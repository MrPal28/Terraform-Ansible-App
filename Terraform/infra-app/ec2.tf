resource "aws_default_vpc" "default"{

}

resource "aws_security_group" "infra_app_sg"{
    name        = "${var.env}-infra-app-sg"
    description = "Allow SSH Access"
    vpc_id = aws_default_vpc.default.id

    #inbound rule
    ingress{
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "SSH ACCESS"
    }
    ingress{
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "HTTP ACCESS"
    }

    ingress{
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "HTTPS Access"
    }
    #outbound rule
    egress{
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
        description = "Allow all outbound traffic"
    }

    tags = {
        name = "allow_ssh"
    }
}


resource "aws_instance" "infra_app_server" {

    count = var.ec2_instance_count #Meta Argument to create multiple instances

    depends_on = [aws_security_group.infra_app_sg, aws_key_pair.terraform_key]

    key_name = aws_key_pair.terraform_key.key_name
    security_groups = [aws_security_group.infra_app_sg.name]
    instance_type = var.ec2_instance_type
    ami = var.ec2_ami

    root_block_device{
        volume_size =  var.ec2_default_storage_size 
        volume_type = var.ec2_storage_type
    }   

    tags = {
        Name = "${var.env}-infra-app-ec2"
        Environment = var.env
    }
}