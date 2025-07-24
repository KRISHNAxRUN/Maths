from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8405058082:AAFyfgpmbec8iTUpfnPDhxUqKe3L9Zfr6RM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        # 👇 Invite Button
        [InlineKeyboardButton("👫 Invite", url="https://t.me/mathsolutionmkr")],

        # 👇 Exercise Buttons
        [InlineKeyboardButton("📘 Ex 1.1", url="https://youtu.be/nd8-akvdnIw?si=ZWA2qQPetHCBpJd5")],
        [InlineKeyboardButton("📘 Ex 1.2", url="https://youtu.be/uuKHJS8zudE?si=u1pXkePQJIsVxA1_")],
        [InlineKeyboardButton("📘 Ex 1.3", url="https://youtu.be/ccMvTsevjpo?si=Og8SxPgsXCXEQLrS")],
        [InlineKeyboardButton("📘 Ex 1.4", url="https://youtu.be/faklWT5XMPU?si=YLoJ3WAnHqe6VflE")],
        [InlineKeyboardButton("📘 Ex 1.5", url="https://youtu.be/YOJ3SzgDjiA?si=crq313yzm0Ez0kkW")],
        [InlineKeyboardButton("📘 Ex 2.1", url="https://youtu.be/AgpUyf-MWGs?si=CVaqqEI0I9LY1FUE")],
        [InlineKeyboardButton("📘 Ex 2.2", url="https://youtu.be/btfWIfCmkmE?si=VOXInp3Iq5eGa0pn")],
        [InlineKeyboardButton("📘 Ex 2.3", url="https://youtu.be/xLOBjRMwlJI?si=JkX3uhfE0FBX2kPB")],
        [InlineKeyboardButton("📘 Ex 2.4", url="https://youtu.be/BGx6Q_2LJT4?si=0kWJZEo0M7tAtJ6V")],
        [InlineKeyboardButton("📘 Ex 3.1", url="https://youtu.be/Sf7L6r7EWWo?si=TEUIWNLHZnR6tEbvS")],
        [InlineKeyboardButton("📘 Ex 3.2", url="https://youtu.be/Sf7L6r7EWWo?si=TEUIWNLHZnR6tEbvS")],
        [InlineKeyboardButton("📘 Ex 4.1", url="https://youtu.be/aPpGKDPTA58?si=j44ksEIfboPekiuf")],
        [InlineKeyboardButton("📘 Ex 4.2", url="https://youtu.be/5BhZM5m33U8?si=JdEPPkU1BisoljM5")],
        [InlineKeyboardButton("📘 Ex 5.1", url="https://youtu.be/Uvzkz2_G91A?si=5KiaoFd4dUSVBCzs")],
        [InlineKeyboardButton("📘 Ex 6.1", url="https://youtu.be/OgX2XGt1bhU?si=1S7z_6NZWjgpeNgu")],
        [InlineKeyboardButton("📘 Ex 6.2", url="https://youtu.be/zKpHn_GiEmA?si=SjV1mfeGlorSlSMo")],
        [InlineKeyboardButton("📘 Ex 7.1", url="https://youtu.be/n5cof3-vx2o?si=Kd5ydL-mRcYkde2S")],
        [InlineKeyboardButton("📘 Ex 7.2", url="https://youtu.be/LEMcD1-hT_c?si=7chJXC94cItGiStO")],
        [InlineKeyboardButton("📘 Ex 7.3", url="https://youtu.be/XXEZvx84e9E?si=pqcPr14SnUylEQcG")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📚 *9th Class Maths NCERT Exercise Videos:*\n\nनीचे से कोई भी Exercise चुनें:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
