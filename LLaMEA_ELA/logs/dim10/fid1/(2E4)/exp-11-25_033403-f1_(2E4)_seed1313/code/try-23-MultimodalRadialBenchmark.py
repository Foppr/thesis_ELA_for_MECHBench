import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term for global convergence
        polynomial = 0.1 * np.sum(x**4)
        
        # Trigonometric multimodal components
        trig = 0.0
        for i in range(self.dim):
            trig += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            trig += 0.5 * np.sin(5 * x[i])**2
            # Cross-dimensional interactions
            if i > 0:
                trig += 0.3 * np.cos(x[i-1] + x[i]) * np.sin(0.5 * x[i-1] - x[i])
        
        # Radial basis function components for local minima
        radial = 0.0
        centers = np.linspace(-4, 4, 9)  # 9 centers from -4 to 4
        for center in centers:
            radial += np.exp(-0.5 * np.sum((x - center)**2))
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.2 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j])
        
        # Combine all components
        return polynomial + trig + radial + interaction