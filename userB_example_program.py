{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMCWFEHDbGoulLajTy+rSVD"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":4,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"P-r3S6mumD43","executionInfo":{"status":"ok","timestamp":1730503374890,"user_tz":-180,"elapsed":509,"user":{"displayName":"asif khan","userId":"12677528117336361548"}},"outputId":"1fae8b6d-6bc2-4fec-ed5e-2cb136411ffd"},"outputs":[{"output_type":"stream","name":"stdout","text":["Hi there, Bob\n"]}],"source":["# User B's Example Notebook\n","\n","def format_string(name):\n","    return f\"Hi there, {name}\"  # Intentional error: missing exclamation mark\n","\n","if __name__ == \"__main__\":\n","    user_name = \"Bob\"\n","    print(format_string(user_name))\n"]}]}