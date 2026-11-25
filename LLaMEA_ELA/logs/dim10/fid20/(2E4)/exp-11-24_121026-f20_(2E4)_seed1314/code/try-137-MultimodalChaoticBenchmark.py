import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        centers = np.linspace(-1, 1, min(10, self.dim))
        if self.dim > 10:
            # Generate random centers for higher dimensions
            np.random.seed(42)
            centers = np.random.uniform(-1, 1, self.dim)
        
        # Radial basis with chaotic width modulation
        rbfs = []
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim <= 10 else np.random.uniform(-1, 1)
            sigma = 0.4 + 0.4 * np.sin(15 * center + np.pi/4)  # Enhanced chaotic width modulation
            rbfs.append(np.exp(-np.sum((x_norm - center)**2) / (2 * sigma**2)))
        
        # Add chaotic phase term for multimodality with enhanced complexity
        phase = np.sum(np.sin(20 * x_norm + np.sin(10 * x_norm))**2 + 
                      0.5 * np.sin(8 * x_norm + np.sin(3 * x_norm))**2)
        
        # Enhanced polynomial terms with chaotic coupling
        poly_term = np.sum(0.8 * x_norm**4 + 0.3 * x_norm**3 - 0.4 * x_norm**2 + 0.1 * x_norm)
        
        # Improved chaotic coupling between dimensions with varying frequencies
        coupling = 0.4 * np.sum(np.sin(15 * x_norm[:-1]) * np.cos(10 * x_norm[1:]) + 
                               0.3 * np.sin(7 * x_norm[:-1]) * np.cos(5 * x_norm[1:]))
        
        # Enhanced chaotic sinusoidal modulation with multiple frequency components
        chaotic_mod = np.sum(np.sin(25 * x_norm + np.sin(8 * x_norm) + np.sin(3 * x_norm)) * 
                            np.cos(15 * x_norm + np.sin(9 * x_norm) + np.sin(4 * x_norm)))
        
        # Additional chaotic basin structure with adaptive scaling
        basin_term = 0.2 * np.sum(np.sin(30 * x_norm)**2 * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Final multimodal landscape with improved convergence properties
        return (np.sum(rbfs) + 0.6 * phase + 0.4 * poly_term + 
                0.3 * coupling + 0.2 * chaotic_mod + 0.1 * basin_term)