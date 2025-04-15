import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('deepseekcode.generateCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor');
            return;
        }

        const document = editor.document;
        const selection = editor.selection;
        const currentLine = document.lineAt(selection.start.line).text;

        const match = currentLine.match(/(?:#|\/\/|--)\s*generate:\s*(.*)/i);
        if (!match) {
            vscode.window.showErrorMessage('No valid prompt comment found (e.g., # generate: sort a list)');
            return;
        }

        const prompt = match[1].trim();
        const languageId = document.languageId;

        try {
            const res = await axios.post('http://localhost:5001/generate', {
                prompt,
                language: languageId
            });

            const generated = res.data.response;

            editor.edit(editBuilder => {
                const insertPosition = new vscode.Position(selection.start.line + 1, 0);
                editBuilder.insert(insertPosition, generated + '\n');
            });
        } catch (err) {
            vscode.window.showErrorMessage('Error talking to the backend.');
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

