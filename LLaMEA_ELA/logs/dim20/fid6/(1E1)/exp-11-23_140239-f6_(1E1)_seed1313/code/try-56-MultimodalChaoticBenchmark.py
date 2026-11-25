import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multimodal chaotic components with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 6)):
            # Periodic chaotic modulation
            freq = i * 0.5
            amp = 2.0 / (i + 1)
            
            # Create a periodic chaotic term using sine and cosine components
            phase = np.sum(x[:min(i, self.dim)] * np.pi / (i + 1))
            chaotic_term = amp * np.sin(freq * x[i-1] + phase) * np.cos(freq * x[i-1] + phase)
            
            # Add to result with exponential decay influence
            result += chaotic_term * np.exp(-0.1 * i)
            
            # Add periodicity in higher dimensions
            if i > 1 and self.dim >= i:
                periodic_component = 1.5 * np.sin(freq * x[i-1] + i) ** 2
                result += periodic_component
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.4 * x[i]**6 - 2.0 * x[i]**4 + 2.5 * x[i]**2
        
        # Introduce noise with varying intensity based on dimensionality
        noise = 0.1 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        return result + noise