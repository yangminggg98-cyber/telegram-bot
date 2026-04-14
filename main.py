import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8796149819:AAGDqu5Z_ZWxJ6HOC-Cu612Hao6YEM8yqew"
PAYMENT_LINK = "https://app.paymento.io/payment-link/0095857262744639899d206b45e41412"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "欢迎使用会员代开机器人！\n\n发送 /buy 获取支付链接"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"点击下方链接完成支付：\n\n{PAYMENT_LINK}\n\n付款后自动开通会员"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("命令：/start - 欢迎，/buy - 购买，/help - 帮助")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()