{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T_-l2hhXIJut"
      },
      "source": [
        "**PROGRAMMING LANGUAGE ?**\n",
        "\n",
        "- It is a medium to interact or communicate with machines(your systems)\n",
        "\n",
        "- ex -> Python , Java , C , C++ , R , Ruby , etc.....\n",
        "\n",
        "-**Syntax -** rule or a way to write any programming language\n",
        "\n",
        "-**keywords -** pre-defined or pre-reserved words which is already having some special meaning or some task to perform (ex - if , else , for , while ....etc)\n",
        "\n",
        "-**Comments -** non-executable part of the code  (these are just used to add some useful notes or some additional information)\n",
        "\n",
        "**how to write a comment in python ? -** # write your comment\n",
        "\n",
        "**multi-line comment in python ?-** '''                 '''"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5sWv9n23JQkl"
      },
      "source": [
        "#**WHAT IS PYTHON AND WHY PYTHON??**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "F47Jpt1hcuYu"
      },
      "source": [
        "Python is a **high level programming language** (designed in such a way that it is easy to read and understand) which is used in many fields such as Data Science , Web development , Cloud infrastructure , Cyber Security .\n",
        "\n",
        "- It was developed by - **Guido Van Rossum** in **1991**\n",
        "\n",
        "- Why name Python?\n",
        "\n",
        "- It came from the name of a show - **\"Monty Python's Flying Circus\"**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "55I_sp24Fj5K"
      },
      "outputs": [],
      "source": [
        "# FEATURES OF PYTHON -\n",
        "# 1- It's syntax is easy ---(somwhere it's syntax is similar to english)\n",
        "# 2- It is an free and open source language\n",
        "# 3- It is an interpreted language - (implementation is done line by line)\n",
        "# 4- It is a case sensitive language - (upper case and lower case are treated differently)\n",
        "# 5- It is simple (easy to learn and understand)\n",
        "# 6- It is a cross platform language - (use it on windows , mac , linux ....)\n",
        "# 7- It has various in-built libraries in it - (ex - numpy , pandas , seaborn , matplotlib)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NlML6LQ5f7NI"
      },
      "source": [
        "*first program in python* - how to print or display anything in python"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rfakd9ITgDPV",
        "outputId": "c69acc06-1c60-4432-8b18-9eab9e946581"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Priti\n"
          ]
        }
      ],
      "source": [
        "print('Priti')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BP0bW1IKgSTb",
        "outputId": "1fa3a020-9a26-4173-bb96-2799a7800f8a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "hello world\n"
          ]
        }
      ],
      "source": [
        "print(\"hello world\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "id": "SfC4bUsYgiIA",
        "outputId": "0d170ae7-e202-4f08-9b57-88e089315943"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "first program\n",
            "10\n",
            "how are you?\n"
          ]
        },
        {
          "ename": "NameError",
          "evalue": "name 'Print' is not defined",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_1990/3756745080.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'how are you?'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mPrint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'first class of python'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'hello'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'Print' is not defined"
          ]
        }
      ],
      "source": [
        "print(\"first program\")\n",
        "print(10)\n",
        "print('how are you?')\n",
        "Print('first class of python')\n",
        "print('hello')\n",
        "# above examples shows the implementation of interpretor language and case sensitivity"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qHAUgx3ngmp4"
      },
      "outputs": [],
      "source": [
        "# write a python program to print your name and city name"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yiCklxJzR2hU"
      },
      "source": [
        "**VARIABLES**\n",
        "\n",
        "- A name to which we assign or give some values. They act as a placeholder which holds some value.\n",
        "\n",
        "**Rules for writing a variable name**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7_CtJfUHS3rF"
      },
      "source": [
        "1- a variable name can't start with a digit/number"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yjuocJHxTJSz"
      },
      "outputs": [],
      "source": [
        "# syntax -> variablename = data/value which you want to assign"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "MRp0CNlZTQ_6",
        "outputId": "7514dd08-20ad-47cd-fb4e-f367d6302e8c"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "invalid decimal literal (2054607335.py, line 1)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_6576/2054607335.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    7a = 'aarav'\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid decimal literal\n"
          ]
        }
      ],
      "source": [
        "7a = 'aarav'\n",
        "7a # error"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g2deogXvTI3S"
      },
      "source": [
        "2- a variable name can start with alphabet (lower case or upper case) or underscore"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "Vfoq0amNTwGz",
        "outputId": "d0cd1e04-76d3-489d-c00e-c08006e13985"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Pawan'"
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "abc = 'Pawan'\n",
        "abc"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G9DudIM4Tyqu",
        "outputId": "ecb4a625-baa7-4c01-ae8d-e17eb13dc613"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10\n"
          ]
        }
      ],
      "source": [
        "a = 10\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "5-WcAQofT1Mv",
        "outputId": "e824ed6a-13d0-4cab-cc65-0dee9d49b49b"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'python'"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Ab = 'python'\n",
        "Ab"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "naiaiZlKT5Hj",
        "outputId": "da90da1b-0de4-4efb-a625-2f90a707dd42"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'good morning'"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "_a1 = 'good morning'\n",
        "_a1"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gst0Ek2uUExT"
      },
      "source": [
        "3- a variable name can't have any special character or any special symbols (ex - @ , # , $ , % , ^ ,&...) except underscore"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "nZRXutJyT_7H",
        "outputId": "0f8904c9-eea2-4f15-dd87-962fc071ec65"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'second class'"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "a_b = 'second class'\n",
        "a_b"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "y7DxmXrzUfeU",
        "outputId": "42f3d236-0061-4192-a57e-65e6a3dcdfa0"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "cannot assign to expression here. Maybe you meant '==' instead of '='? (208906097.py, line 1)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_6576/208906097.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    a@b = 12\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m cannot assign to expression here. Maybe you meant '==' instead of '='?\n"
          ]
        }
      ],
      "source": [
        "a@b = 12\n",
        "a@b # error - because variable name can't have any special charcter or symbol"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ChQfNPG6VERG"
      },
      "source": [
        "4- a variable name can't have any space between them"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "abSrjBFmUmn5",
        "outputId": "46927576-feed-418a-c6fb-7b58aaf14f80"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "invalid syntax (1202742622.py, line 1)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_6576/1202742622.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    a b = 'python'\u001b[0m\n\u001b[0m      ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "a b = 'python'\n",
        "a b # error"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "v6GLeLfAVNLM"
      },
      "source": [
        "5- variable can be alphanumeric (combination of alphabets and numbers)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "eP-ob-kbVK3T",
        "outputId": "d0a5d1ca-f2ae-492a-c7bc-7b37e516b30e"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'hello'"
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "abc12 = 'hello'\n",
        "abc12"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VaLXKBI0Vbev"
      },
      "source": [
        "6- a variable name can't be a keyword"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "_Fk4Qj9pVVPA",
        "outputId": "8716fc5e-5fe6-4371-bedf-70ce54676c21"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "invalid syntax (3230749096.py, line 1)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_6576/3230749096.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    while = 'a'\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "while = 'a'\n",
        "while       # error"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vs6uS9MEVy2Q",
        "outputId": "a62a96c0-ad22-42c7-aa93-c6de0d86dac7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "name of student - Manya\n",
            "age is - 23\n",
            "marks - 60\n"
          ]
        }
      ],
      "source": [
        "# Create a variable to store the name , age and marks of a student-\n",
        "name = 'Manya'\n",
        "a1 = 23\n",
        "marks = 60\n",
        "print('name of student -' ,name)\n",
        "print('age is -' ,a1)\n",
        "print('marks -',marks)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9uo6ZGp0WVax",
        "outputId": "3029acd8-50fc-4167-a687-d05f24b9885b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "name is - Manya ,age is - 23 ,marks - 60\n"
          ]
        }
      ],
      "source": [
        "# how to print output in a single statement\n",
        "print('name is -',name,',age is -',a1 , ',marks -',marks)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "afPNb9lJXNHB",
        "outputId": "0166a815-d5c6-485e-d221-09ec197a15f4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Manya 23 60\n"
          ]
        }
      ],
      "source": [
        "print(name , a1,marks)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0-RfpZloXwzi"
      },
      "source": [
        "**DATA TYPES -** tells us the type of data a variable is holding\n",
        "\n",
        "- how to check datatype -> **type(variablename)**\n",
        "\n",
        "**what are the data types which are available in python-**\n",
        "\n",
        "1- NUMERIC DATA -> every data which is related to numbers\n",
        "\n",
        "(ex - 3 , 4 ,500 , 10.5 , 99.5.....)\n",
        "\n",
        "- **Integer** , **Float** , **Complex**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aS7URrb0Y7q6"
      },
      "source": [
        "Integer -> whole number / numbers which are not in the form of decimals.\n",
        "\n",
        "- Can be positive or negative\n",
        "\n",
        "- ex - (100 , -28 , -1 , 450 , 14 .......)\n",
        "\n",
        "- it will return the datatype -----> **int**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kqn2-vx1XZnk",
        "outputId": "53eb9aef-9ab1-43b0-959c-dd31e45b5f4c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "execution_count": 26,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "a1 = 98\n",
        "a1\n",
        "type(a1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "khjwdO6yZXcq",
        "outputId": "91730c7b-f98a-4094-93e3-9c7e77225fd3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "-2908\n",
            "<class 'int'>\n"
          ]
        }
      ],
      "source": [
        "b = -2908\n",
        "print(b)\n",
        "print(type(b))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fMnha_ZGZmDi"
      },
      "source": [
        "FLOAT -> any positive or negative decimal number/value\n",
        "\n",
        "- it will return -----> **float**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mwZ5Kw0nZhy1",
        "outputId": "6b242644-9d82-4db0-98f5-17d78221430c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "execution_count": 28,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "x = 9.75\n",
        "type(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pAqNkK0UbVCk",
        "outputId": "23b1255a-ff5b-40dd-8ae3-4f589026c917"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'float'>\n"
          ]
        }
      ],
      "source": [
        "y1 = -2.7\n",
        "print(type(y1))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tFhfrRFfbbOH"
      },
      "source": [
        "COMPLEX -> any number which is written in the form of a + bj\n",
        "\n",
        "- ex - (2+5j , 1+j , 10 + 1j....)\n",
        "\n",
        "- it will return the datatye --------> **complex**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jzjj_53IbX4w",
        "outputId": "5747d9ef-8457-4d51-db1b-b7a801f77f36"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(2+2j)"
            ]
          },
          "execution_count": 31,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "x = 2+2j\n",
        "x"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6euIaxeVcFSl",
        "outputId": "f15ac6e1-e6e7-4a43-9bfb-780a59684133"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "complex"
            ]
          },
          "execution_count": 32,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "type(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "KIL6nJ9dcG91",
        "outputId": "7f37714e-ab92-447b-eb8c-eb7de3da3a0c"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "invalid syntax. Maybe you meant '==' or ':=' instead of '='? (1007675760.py, line 1)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_6576/1007675760.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    a = 5 , bj = 2\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Maybe you meant '==' or ':=' instead of '='?\n"
          ]
        }
      ],
      "source": [
        "a = 5 , bj = 2\n",
        "# two variable names can't be written or initialize in a single line"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qaVGgMBkcJre",
        "outputId": "1d981c40-cea3-4c52-bcb4-a29f006f2620"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "complex"
            ]
          },
          "execution_count": 39,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "a2 = 2 - 7j\n",
        "type(a2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8G1zxjCwgOxh",
        "outputId": "a90c952d-f82d-48f6-cc99-d33e96c38c3b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "(3+4j)\n",
            "<class 'complex'>\n",
            "(5+4j)\n",
            "<class 'complex'>\n"
          ]
        }
      ],
      "source": [
        "complex1=3+4j\n",
        "complex2=complex(5,4)\n",
        "print(complex1)\n",
        "print(type(complex1))\n",
        "print(complex2)\n",
        "print(type(complex2))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZUGW1FEfcxlK"
      },
      "source": [
        "2- STRINGS -> sequence of characters which is enclosed in single , double or triple quotes\n",
        "\n",
        "- it will return the datatype as -----> **str**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J16dbXm7cWpU",
        "outputId": "d28e2edd-3ec9-4f5e-d882-9dbcdf2cec80"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Manish\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "j = 'Manish'\n",
        "print(j)\n",
        "type(j)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QAc2HSj4dULS",
        "outputId": "d292f6ac-0f18-4e8f-9c96-df1be50baecb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'float'>\n",
            "<class 'int'>\n",
            "<class 'str'>\n",
            "<class 'str'>\n"
          ]
        }
      ],
      "source": [
        "b1 = 9.5\n",
        "b2 = 10\n",
        "b3 = 'hello python'\n",
        "b4 = '60'\n",
        "print(type(b1))\n",
        "print(type(b2))\n",
        "print(type(b3))\n",
        "print(type(b4))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "p3PndjwnefEv"
      },
      "source": [
        "3- BOOLEAN DATA TYPE - It has two values - **True** and **False**\n",
        "\n",
        "- it will return the data type --------> **bool**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j1q6VSRtd0IF",
        "outputId": "2d727d83-4106-4396-f0c5-e3f980bc4040"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n",
            "<class 'bool'>\n"
          ]
        }
      ],
      "source": [
        "x = False\n",
        "print(x)\n",
        "print(type(x))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IkBnt73CfWOO",
        "outputId": "e24dee05-830d-4add-8d94-b5e44e6353a4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ],
      "source": [
        "x1 = 'True'\n",
        "print(type(x1))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "LxF4OtsQfbsX",
        "outputId": "d367590c-7c91-4b13-89f1-2d797af3cfbf"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "' This is the way to write a multiline comment in python '"
            ]
          },
          "execution_count": 51,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "''' This is the way to write a multiline comment in python '''"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KYDES5jOjNYx"
      },
      "source": [
        "**OPERATORS**\n",
        "\n",
        "- Symbols which are used to perform some task or some operations\n",
        "\n",
        "1- Arithmetic Operators\n",
        "\n",
        "2- Comparison Operators\n",
        "\n",
        "3- Logical Operators\n",
        "\n",
        "4- Assignment Operators\n",
        "\n",
        "5- Membership Operators\n",
        "\n",
        "6- Identity Operators"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-KVPXt3Yj85j"
      },
      "source": [
        "**1- Arithemtic Operators -** used for performing mathematical calculations - ex - addition , subtraction , multiplication , divide , exponential , floor division , modulous"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XuKkHd8xhnYW",
        "outputId": "6782606a-3f75-4ee6-a3a8-61a7541636d5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "556\n"
          ]
        }
      ],
      "source": [
        "# addition\n",
        "a1 = 100\n",
        "a2 = 456\n",
        "print(a1+a2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c3Hk8QYUkXov",
        "outputId": "e3d286a7-776c-4c48-bd66-6b12d2445bfe"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "-356"
            ]
          },
          "execution_count": 54,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# subtraction\n",
        "a1-a2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bKkNYThxkaha",
        "outputId": "bbbcc271-5301-4cd8-af61-8ce453c11f99"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "multiplication - 100\n"
          ]
        }
      ],
      "source": [
        "# multiplication\n",
        "x = 10\n",
        "y = 10\n",
        "print(\"multiplication -\",x*y)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "29hUSBzFkfye",
        "outputId": "d6a6dbd7-d248-42df-b29b-ead2e968cbfe"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "division -  11.5\n"
          ]
        }
      ],
      "source": [
        "# division ---------> / return type ------float\n",
        "a = 23\n",
        "b = 2\n",
        "print('division - ',a/b)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VOHX8nQbk7GS",
        "outputId": "f22c332e-9c19-4c33-9a74-641e633e3d24"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "floor division -  11\n"
          ]
        }
      ],
      "source": [
        "# floor division -------> // ----> return type ----------- int\n",
        "a = 23\n",
        "b = 2\n",
        "print('floor division - ',a//b)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E-GALh77lDsB",
        "outputId": "438bf61f-6a1d-478e-cf60-1ded404a94b2"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "execution_count": 59,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# modulous -> % -------- return the remainder\n",
        "x1 = 37\n",
        "x2 = 3\n",
        "x1%x2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gkrSyrsAmdoH",
        "outputId": "96cc8354-f629-49f0-a5b3-c5647a477336"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "2\n"
          ]
        }
      ],
      "source": [
        "y1 = 37\n",
        "print(y1%5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UrDWwNFLmjxL",
        "outputId": "138dc2bb-c241-4851-89b2-d93f81bb37fb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "32"
            ]
          },
          "execution_count": 61,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# exponential operator ---->**---- returns the power/exponential value of a number\n",
        "a = 2\n",
        "b = 5\n",
        "a**b   # (2**5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U1x2n-kZnFAw",
        "outputId": "62ef9fa7-5a93-446b-d4be-4e89a3baf298"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "390625\n"
          ]
        }
      ],
      "source": [
        "print(5**8)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d9I2NHJsnoPw"
      },
      "source": [
        "**2- Comparison operators -** used to compare the values\n",
        "\n",
        "- return the answer in boolean values\n",
        "\n",
        "- equals ------> ==\n",
        "\n",
        "- not equals ------> !=\n",
        "\n",
        "- greater than -------> > , greater than equal to -----> >=\n",
        "\n",
        "- less than --------> < , less than equal to -------> <="
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5gh55YR-nHYf",
        "outputId": "61506e30-f2d8-4e1c-a7a1-eea43ba018ed"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "i = 982\n",
        "j = 109\n",
        "print(i==j)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-2soy7Fzoagx",
        "outputId": "a9cf738f-d360-49cb-dc6f-eab195fd38c9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 64,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "i<j"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y2agWRylobvt",
        "outputId": "700939bd-cc47-44c1-c430-feba99075838"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 65,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "i>j"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2AtSvXbZocv7",
        "outputId": "83d0c46c-c5b5-4117-ac53-174cd0f82fef"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 66,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "i!=j\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nMbpz9XvomXF"
      },
      "source": [
        "**3- Assignment Operators -** used to assign or give some value"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v0a0jhyRohDt",
        "outputId": "ebd22a42-37b3-4c0e-b439-beeae530b980"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "aarav\n"
          ]
        }
      ],
      "source": [
        "v1 = 'aarav'\n",
        "print(v1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MgCqUeb-oySD",
        "outputId": "3ca347bd-53ed-43ca-b0eb-bcdb2ad48de8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "aarav\n"
          ]
        }
      ],
      "source": [
        "v2 = v1\n",
        "print(v2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ydVF1qGCo8zJ",
        "outputId": "c1bf9c38-0994-48f1-f069-9073cc01e2e8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "60\n"
          ]
        }
      ],
      "source": [
        "a = 50\n",
        "a += 10 # a = a+10\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XAwvVCPFpPpA"
      },
      "source": [
        "**4- Logical Operators -** used to combine multiple statemnets or conditions\n",
        "\n",
        "- **and** , **or** , **not**\n",
        "\n",
        "- output will be boolean value"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vdhSL-Nop8jT"
      },
      "outputs": [],
      "source": [
        "# and ---> if both the statements or conditions are true then only it will return true otherwise false"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YrDhBGkwp7Ip"
      },
      "source": [
        "![image.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hdn47FXMpMuM",
        "outputId": "530ba610-c9f2-47d4-f54c-79c16ae2e069"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 70,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "n1 = 80\n",
        "n2 = 75\n",
        "ans = (n1>5) and (n2>n1)\n",
        "ans"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WO9Hcud_qYXE"
      },
      "outputs": [],
      "source": [
        "# or ------> it returns true if atleast one statement is true other wise it will return false"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z9zcuG_jqxUa"
      },
      "source": [
        "![image.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v4Q185K2qyJq",
        "outputId": "56cc9cac-9113-48e3-e653-0cab9dd0745d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 71,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "c1 = 10\n",
        "c2 = 5\n",
        "(c1>c2) or (c2 <c1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ohecQTYyrKZO"
      },
      "outputs": [],
      "source": [
        "# not ------> it will reverse the output\n",
        "# output = True ---> False\n",
        "# output = False ---> True"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1nqNDpxNrYME",
        "outputId": "f77733b6-cf55-4b78-d97b-54c10ac08c16"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "result is - True\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "a = 100\n",
        "b = 70\n",
        "res = (a>80) and (a>b)\n",
        "print(\"result is -\",res)\n",
        "print(not(res))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MT87JBWQrpoz"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
