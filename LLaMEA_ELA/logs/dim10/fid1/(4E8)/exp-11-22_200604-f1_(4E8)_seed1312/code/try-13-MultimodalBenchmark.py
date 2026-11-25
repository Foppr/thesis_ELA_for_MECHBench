import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Add a more complex multimodal component with multiple peaks
        f3 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Add a small noise term to make the landscape more complex
        noise = 0.05 * np.random.random()
        
        return f1 + 0.15 * f2 + 0.05 * f3 + noise