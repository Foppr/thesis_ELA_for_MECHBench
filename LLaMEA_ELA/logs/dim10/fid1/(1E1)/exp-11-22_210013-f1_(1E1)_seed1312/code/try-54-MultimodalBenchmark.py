import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with chaotic noise
        quadratic = 0.1 * np.sum(x**2) + 0.02 * np.random.rand() * np.sin(100 * np.sum(x))
        
        # Multi-scale sinusoidal oscillations with chaotic phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(15 * x[i]) * np.exp(-0.2 * (x[i] - 1)**2)
            sinusoidal += 0.4 * np.cos(8 * x[i]) * np.sin(5 * x[(i + 1) % self.dim])
            sinusoidal += 0.2 * np.sin(12 * x[i]) * np.cos(7 * x[(i + 2) % self.dim])
        
        # Complex non-separable multimodal term with fractal-like interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.8 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            multimodal += 0.3 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.2 * np.sin(3 * x[i]) * np.sin(3 * x[(i + 2) % self.dim])
            multimodal += 0.1 * x[i]**3 * np.cos(3 * x[(i + 3) % self.dim])
            multimodal += 0.05 * np.sin(9 * x[i]) * np.cos(6 * x[(i + 4) % self.dim])
        
        # Global structure with chaotic cross-dimensional interactions
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**4
            global_structure += 0.6 * np.sin(8 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            global_structure += 0.4 * np.cos(5 * x[i]) * np.sin(9 * x[(i + 2) % self.dim])
            global_structure += 0.3 * np.sin(10 * x[i]) * np.cos(8 * x[(i + 3) % self.dim])
        
        # High-frequency chaotic noise component with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(50 * x[i]) * np.cos(40 * x[(i + 1) % self.dim])
            noise += 0.2 * np.sin(70 * x[i]) * np.cos(60 * x[(i + 2) % self.dim])
        
        # Additional chaotic cross-dimensional coupling term
        coupling = 0.0
        for i in range(self.dim):
            coupling += 0.15 * np.sin(20 * x[i] + 0.5 * x[(i + 1) % self.dim]) * np.cos(15 * x[(i + 2) % self.dim])
        
        # Improved fitness with enhanced scaling and complex interactions
        return 0.9 * quadratic + 1.4 * sinusoidal + 1.8 * multimodal + 1.3 * global_structure + 0.7 * noise + 0.5 * coupling