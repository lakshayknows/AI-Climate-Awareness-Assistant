# 🌍 AI Climate Awareness Assistant

> **Transforming climate information into actionable awareness through AI-powered summaries, interactive quizzes, and personalized eco-actions.**

**🚀 Live Demo:** [https://ai-climate-awareness.streamlit.app/](https://ai-climate-awareness.streamlit.app/)

---

## 🌱 About This Project

The AI Climate Awareness Assistant is an innovative tool designed to bridge the gap between complex climate research and public understanding. By leveraging advanced language models through OpenRouter, this application transforms dense climate articles into digestible insights and actionable steps for environmental impact.

**Why This Matters:**
Climate change information is often locked away in academic papers and technical reports that are difficult for the general public to understand and act upon. This tool democratizes climate knowledge by making it accessible, engaging, and immediately actionable.

## ✨ Key Features

### 📝 **Intelligent Summarization**
- Converts complex climate articles into clear, jargon-free summaries
- Preserves critical information while making it accessible to everyone
- Perfect for staying informed without getting overwhelmed by technical details

### 🎯 **Interactive Awareness Quizzes**
- Generates custom quizzes based on article content
- Progressive difficulty levels (easy → medium → hard)
- Helps reinforce learning and test understanding
- Great for educational purposes and knowledge retention

### 🌍 **Personalized Eco-Actions**
- Suggests specific, implementable actions based on article themes
- Categorized by impact area: energy, waste, transport, water, general
- Shows potential environmental impact of each action
- Transforms awareness into concrete steps

### 📂 **Flexible Input Options**
- Upload files: `.txt`, `.pdf`, `.docx`
- Direct text input for quick analysis
- Seamless processing across different content formats

## 🛠️ Technology Stack

- **Frontend:** Streamlit (intuitive web interface)
- **AI/ML:** LangChain + OpenRouter (GPT models)
- **Document Processing:** PyPDF2, python-docx
- **Data Validation:** Pydantic (structured outputs)
- **Deployment:** Streamlit Cloud

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenRouter API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Climate-Awareness-Assistant.git
   cd AI-Climate-Awareness-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "OPENROUTER_API_KEY=your_api_key_here" > .env
   echo "OPENROUTER_BASE_URL=https://openrouter.ai/api/v1" >> .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Environment Configuration

Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

## 📁 Project Structure

```
AI-Climate-Awareness-Assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── LICENSE               # Apache 2.0 License
├── README.md             # This file
│
├── chains/               # AI processing chains
│   ├── summarizer.py     # Article summarization logic
│   ├── quiz_generator.py # Quiz creation with difficulty levels
│   ├── recommender.py    # Eco-action recommendations
│   └── merge.py          # Parallel processing chain
│
├── utils/                # Utility modules
│   ├── config.py         # Configuration management
│   ├── formatter.py      # Streamlit display formatting
│   └── loaders.py        # File processing utilities
│
└── templates/            # Prompt templates
    ├── template1.json    # Summarization prompt
    └── template_gen.py   # Template generation script
```

## 🎯 How It Works

1. **Input Processing:** Upload or paste climate-related articles
2. **AI Analysis:** Advanced language models analyze the content
3. **Multi-Modal Output:** 
   - Generate plain-language summaries
   - Create difficulty-graded quizzes
   - Suggest personalized eco-actions
4. **Interactive Display:** User-friendly tabs for easy navigation

## 🌟 Use Cases

- **📚 Education:** Teachers creating climate awareness materials
- **📰 News Consumption:** Readers wanting quick, actionable insights
- **🏢 Organizations:** Companies developing sustainability training
- **🎓 Research:** Academics making their work more accessible
- **👥 Community Groups:** Environmental activists spreading awareness

## 🔧 Advanced Features

### Parallel Processing
The application uses LangChain's `RunnableParallel` to process all three outputs simultaneously, ensuring fast response times even with complex articles.

### Structured Data Validation
Pydantic models ensure consistent, reliable outputs:
- Quiz questions with validated difficulty levels
- Eco-actions with proper categorization
- Error handling for robust user experience

### Document Intelligence
Smart file processing that handles various formats while preserving content structure and meaning.

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 **Bug Reports:** Found an issue? Open a GitHub issue
- 💡 **Feature Ideas:** Suggest new capabilities or improvements
- 📝 **Documentation:** Help improve setup instructions or usage guides
- 🔧 **Code Contributions:** Submit pull requests for enhancements

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📊 Performance & Scaling

- **Response Time:** Typically 3-5 seconds for full analysis
- **Article Length:** Optimized for articles up to 5,000 words
- **Concurrent Users:** Scales automatically with Streamlit Cloud
- **API Efficiency:** Smart caching and parallel processing

## 🔒 Privacy & Security

- No article content is permanently stored
- API keys are securely managed through environment variables
- All processing happens in secure, ephemeral sessions
- User uploads are processed locally and not retained

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** for the powerful AI orchestration framework
- **OpenRouter** for democratizing access to advanced language models
- **Streamlit** for making ML applications accessible to everyone
- **Climate Researchers** whose work this tool aims to amplify

## 📞 Support & Contact

- **Live App:** [https://ai-climate-awareness.streamlit.app/](https://ai-climate-awareness.streamlit.app/)
- **Issues:** GitHub Issues tab
- **Developer:** Built with 💚 by Lakshay

---

**🌱 "Small actions, when multiplied by millions of people, can transform the world."**

*Start your climate awareness journey today with AI-powered insights and actionable steps.*
