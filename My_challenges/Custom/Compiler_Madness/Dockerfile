FROM ubuntu

RUN apt update && apt upgrade -yy
RUN apt install python3 python3-pip gcc -yy
RUN pip3 install flask

RUN echo "Hi,\nbro\nYou want flag heh?\n\nflag\nZCTF{Flaggg_Goess_burrr!}" > /flag

COPY app /app
WORKDIR /app

EXPOSE 8002

CMD ["python3", "app.py"]