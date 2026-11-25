import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with structured noise
        quadratic = 0.1 * np.sum(x**2) + 0.01 * np.random.rand()
        
        # Sinusoidal oscillations with chaotic frequency ratios and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(7.3 * x[i]) * np.exp(-0.12 * (x[i] - 1.2)**2)
            sinusoidal += 0.35 * np.cos(5.7 * x[i]) * np.sin(3.1 * x[(i + 1) % self.dim])
        
        # Enhanced multimodal term with increased cross-interactions and higher-order polynomial terms
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.75 * np.sin(4.2 * x[i]) * np.cos(3.8 * x[(i + 1) % self.dim])
            multimodal += 0.3 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.12 * np.sin(2.5 * x[i]) * np.sin(2.3 * x[(i + 2) % self.dim])
            multimodal += 0.08 * x[i]**3 * np.cos(2.7 * x[(i + 3) % self.dim])
        
        # Stronger global structure component with chaotic interaction terms
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2.1)**4
            global_structure += 0.55 * np.sin(6.2 * x[i]) * np.cos(5.3 * x[(i + 1) % self.dim])
            global_structure += 0.4 * np.cos(4.1 * x[i]) * np.sin(7.5 * x[(i + 2) % self.dim])
        
        # High-frequency chaotic noise component with irregular weights
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(26.1 * x[i]) * np.cos(21.7 * x[(i + 1) % self.dim])
        
        # Improved fitness with better scaling and additional complexity
        return 0.85 * quadratic + 1.4 * sinusoidal + 1.8 * multimodal + 1.2 * global_structure + 0.8 * noise