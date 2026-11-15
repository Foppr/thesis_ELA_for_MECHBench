import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian radial basis function components with varying centers and widths
        centers = np.linspace(-0.8, 0.8, 5)
        widths = np.logspace(-1, 1, 5)
        gaussian = np.zeros_like(x_scaled)
        for i, (c, w) in enumerate(zip(centers, widths)):
            gaussian += np.exp(-w * (x_scaled - c)**2) * np.sin(2 * np.pi * (x_scaled - c))
        
        # Trigonometric coupling between dimensions with adaptive frequency modulation
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(3 * np.pi * x_scaled[i]) * np.cos(4 * np.pi * x_scaled[i+1]) * \
                       np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[i+1]**2))
        
        # Adaptive polynomial modulation based on distance from origin
        distance = np.sqrt(np.sum(x_scaled**2))
        poly_mod = 1.0 + 0.5 * np.sin(5 * distance) * (x_scaled**3 + 0.3 * x_scaled**4)
        
        # Sine-cosine hybrid with dynamic phase shift
        hybrid = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * 
                       np.exp(-0.3 * x_scaled**2))
        
        # Dynamic barrier with exponentially varying heights
        barrier_heights = np.exp(np.linspace(0, 2, self.dim))
        barriers = np.sum(barrier_heights * np.exp(-2 * np.abs(x_scaled)) * 
                         np.sin(5 * np.pi * x_scaled)**2)
        
        # Combine all components with dynamic weights
        return 0.3 * np.sum(gaussian) + 0.4 * coupling + 0.2 * np.sum(poly_mod) + \
               0.15 * hybrid + 0.25 * barriers