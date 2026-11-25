import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with chaotic noise
        quadratic = 0.1 * np.sum(x**2) + 0.02 * np.random.rand() * np.prod(x + 1.0)
        
        # Sinusoidal oscillations with chaotic phase shifts and higher frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(9 * x[i]) * np.exp(-0.15 * (x[i] - 1)**2)
            sinusoidal += 0.4 * np.cos(7 * x[i]) * np.sin(5 * x[(i + 1) % self.dim])
            sinusoidal += 0.1 * np.sin(11 * x[i]) * np.cos(8 * x[(i + 2) % self.dim])
        
        # Enhanced multimodal term with stronger cross-interactions and chaotic components
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.8 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            multimodal += 0.3 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.15 * np.sin(3 * x[i]) * np.sin(3 * x[(i + 2) % self.dim])
            multimodal += 0.08 * x[i]**3 * np.cos(3 * x[(i + 3) % self.dim])
            multimodal += 0.05 * np.sin(13 * x[i]) * np.cos(10 * x[(i + 4) % self.dim])
        
        # Modified global structure with chaotic and non-separable components
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**5
            global_structure += 0.6 * np.sin(7 * x[i]) * np.cos(6 * x[(i + 1) % self.dim])
            global_structure += 0.4 * np.cos(5 * x[i]) * np.sin(8 * x[(i + 2) % self.dim])
            global_structure += 0.2 * np.sin(9 * x[i]) * np.cos(7 * x[(i + 3) % self.dim])
        
        # High-frequency chaotic noise component with exponential decay
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(30 * x[i]) * np.cos(25 * x[(i + 1) % self.dim])
            noise += 0.1 * np.sin(35 * x[i]) * np.cos(30 * x[(i + 2) % self.dim])
        
        # Final fitness with chaotic scaling and additional complexity
        return 0.9 * quadratic + 1.4 * sinusoidal + 1.7 * multimodal + 1.2 * global_structure + 0.7 * noise