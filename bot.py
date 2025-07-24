from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8405058082:AAFyfgpmbec8iTUpfnPDhxUqKe3L9Zfr6RM"

# तेरे प्राइवेट चैनल का ID
CHANNEL_CHAT_ID = -1002810672750

# 1.1 वीडियो का मैसेज ID
EX_1_1_MESSAGE_ID = 3

# /start कमांड पर बटन दिखाना
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Ex 1.1 सभी प्रश्न", callback_data="ex_1_1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👇 नीचे दिए गए बटन पर क्लिक करें Ex 1.1 वीडियो देखने के लिए:", reply_markup=reply_markup)

# जब बटन दबाया जाए
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ex_1_1":
        await context.bot.forward_message(
            chat_id=query.message.chat_id,
            from_chat_id=CHANNEL_CHAT_ID,
            message_id=EX_1_1_MESSAGE_ID
        )

# बॉट को रन करो
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.run_polling()