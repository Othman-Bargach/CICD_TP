resource "aws_instance" "app_server" {
  ami           = "ami-0ba9cfae65a212e98" #AMI Ubuntu
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]

  key_name = "TP DevOps SSH Key" #Nom de la clé sur AWS 

  associate_public_ip_address = true

  tags = {
    Name = "EC2-TP-DevOps"
  }
}

output "public_ip" {
  value = aws_instance.app_server.public_ip
}