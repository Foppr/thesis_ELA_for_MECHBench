import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditionally scaled coefficients
        result = 0.5 * np.sum(x**2)
        
        # Enhanced chaotic sinusoidal components with non-linear frequency modulation and phase shifts
        for i in range(self.dim):
            freq = 4 + 3 * np.sin(0.7 * x[i]) + 0.5 * np.cos(1.3 * x[i])
            phase = 0.3 * np.sin(2 * x[i])
            result += 0.3 * np.sin(freq * x[i] + phase) * np.cos(3 * x[i] + 0.7 * np.sin(x[i]))
        
        # Stronger asymmetric cross-dimensional interactions with variable coupling strengths and additional non-linearity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * (i + 1) / (j + 1) * np.sin(0.5 * x[i])
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Non-uniform penalty term with multiple local minima and enhanced complexity
        result += 0.1 * np.sum((x - 2.0)**2 * (1 + 0.5 * np.sin(5 * x)) * (1 + 0.3 * np.cos(3 * x)))
        
        # Additional chaotic oscillation component with higher frequency and amplitude
        chaos_term = 0.2 * np.sum(np.sin(5 * x) * np.cos(9 * x) * np.tanh(x))
        result += chaos_term
        
        # Add a global shaping term to increase the complexity of the landscape
        global_shape = 0.1 * np.sum(np.sin(0.3 * x) * np.cos(0.7 * x)) * np.exp(-0.05 * np.sum(x**2))
        result += global_shape
        
        return result