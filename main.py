
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from discordwebhook import Discord


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def get_response(request: Request):
    # try:
    email = request.query_params.get('mail')
    print('email= ' + email)
    # except:
    #     print('no parameters')
    #     with open('./templates/thanksPage.html', "r", encoding="utf-8") as file:
    #         html_content = file.read()
    #     print('exception0')
    #     return HTMLResponse(content=html_content)

    # try:
    answer = request.query_params.get('code')
    print('code= ' + answer)
    # except:
    #     print('no parameters')
    #     with open('./templates/thanksPage.html', "r", encoding="utf-8") as file:
    #         html_content = file.read()
    #     print('exception1')
    #     return HTMLResponse(content=html_content)

    # answerによってreturnするtemplateを分岐
    # 187=interests, 263=interview と定義する。
    # 263は面談希望。面談予約サイトへリダイレクト
    if answer == '263':
        # with open('./templates/scheduling.html', "r", encoding="utf-8") as file:
        #     html_content = file.read()
        # return HTMLResponse(content=html_content)
        code = '面談希望'
        post_To_Discode(email, code)
        response = RedirectResponse(url='https://meeting.eeasy.jp/kasai-lab/online')
        return response
    # 187は興味あり。商品紹介LPへリダイレクト
    elif answer == '187':
        code = '興味あり'
        post_To_Discode(email, code)
        response = RedirectResponse(url='https://www.kasai-lab.com/')
        return response
    # 例外としてthanksページを表示させる処理を書いておく。
    else:
        with open('./templates/thanksPage.html', "r", encoding="utf-8") as file:
            html_content = file.read()
        print('exception2')
        return HTMLResponse(content=html_content)


def post_To_Discode(email, code):
    # メールアドレスと回答結果をdiscordに通知する
    post = f"メールから新着の回答がありました！\n確認の上、アクションを設定してください。\nmail: {email}\n回答内容: {code}"
    print(post)
    url = "https://discord.com/api/webhooks/1152857787769045033/DnV-t3r3NlEEq9Xthz5SvOgjZ42qnwFwu8T1VQjia03zR4VBtjrUFWSjDnrVdZbfXB4Y"
    discord = Discord(url=url)
    discord.post(content=post)
    print('discord posted!!')



