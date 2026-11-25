import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine waves with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(np.exp(x[i])) * np.cos(0.5 * np.exp(2 * x[i])) + \
                     0.2 * np.sin(np.exp(1.5 * x[i])) * np.cos(np.exp(x[i] / 2)) + \
                     0.1 * np.sin(np.exp(3 * x[i]))
        
        # Add fractal-like self-similarity using recursive scaling
        for i in range(self.dim):
            f_val += 0.05 * np.sin(10 * x[i]) * np.cos(15 * x[i]) + \
                     0.03 * np.sin(20 * x[i]) * np.cos(25 * x[i])
        
        # Introduce exponential decay interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                f_val += 0.02 * np.exp(-abs(x[i] - x[j])) * np.sin(5 * (x[i] + x[j]))
        
        # Add polynomial coupling terms with varying degrees
        for i in range(self.dim):
            f_val += 0.01 * x[i]**7 + 0.005 * x[i]**9 + 0.002 * x[i]**11
        
        # Include a high-frequency chaotic component
        for i in range(self.dim):
            f_val += 0.15 * np.sin(50 * x[i]) * np.cos(40 * x[i]) + \
                     0.1 * np.sin(60 * x[i]) * np.cos(30 * x[i])
        
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            f_val += 0.02 * np.exp(-0.5 * (x[i] - np.mean(x))**2) + \
                     0.01 * np.exp(-0.3 * (x[i] - np.std(x))**2)
        
        # Add nested local minima using a sum of exponentially modulated sinusoids
        for i in range(self.dim):
            for k in range(1, 8):
                f_val += 0.02 * np.sin(k * x[i]) * np.exp(-k * abs(x[i]))
                
        return f_val