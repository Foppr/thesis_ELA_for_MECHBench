import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = 0.1 * np.sum(x**2)
        
        # Chaotic component with saddle points and periodic attractors
        chaotic = 0.0
        for i in range(self.dim):
            # Saddle point contribution
            chaotic += 0.5 * x[i] * np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            # Periodic attractor component
            chaotic += 0.3 * np.sin(5 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
            # Cross-dimensional interaction
            chaotic += 0.2 * x[i]**3 * np.cos(4 * x[(i + 2) % self.dim])
        
        # Multi-modal structure with embedded local minima
        multimodal = 0.0
        for i in range(self.dim):
            # High-frequency oscillation with varying amplitude
            multimodal += 0.8 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            # Non-separable cubic interaction
            multimodal += 0.4 * x[i] * x[(i + 1) % self.dim]**2
            # Coupled sinusoidal with phase shifts
            multimodal += 0.1 * np.sin(3 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(2 * x[(i + 3) % self.dim])
        
        # Global structure with multiple coexisting basins
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**4 + (x[i] + 2)**4
            global_structure += 0.6 * np.sin(3 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
            # Add non-linear coupling between dimensions
            global_structure += 0.3 * x[i]**2 * np.sin(4 * x[(i + 2) % self.dim])
        
        # Noise component to increase complexity and challenge robustness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(20 * x[i]) * np.cos(15 * x[(i + 1) % self.dim])
            noise += 0.1 * np.sin(30 * x[i]) * np.sin(25 * x[(i + 2) % self.dim])
        
        # Combine all components with appropriate scaling
        return 0.9 * quadratic + 1.4 * chaotic + 1.7 * multimodal + 1.2 * global_structure + 0.8 * noise