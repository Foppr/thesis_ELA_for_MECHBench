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
            sigma = 0.5 + 0.3 * np.sin(10 * center)  # Chaotic width modulation
            rbfs.append(np.exp(-np.sum((x_norm - center)**2) / (2 * sigma**2)))
        
        # Add chaotic phase term for multimodality
        phase = np.sum(np.sin(15 * x_norm + np.sin(7 * x_norm))**2)
        
        # Combine with polynomial terms and chaotic coupling
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2)
        
        # Chaotic coupling between dimensions
        coupling = 0.3 * np.sum(np.sin(12 * x_norm[:-1]) * np.cos(8 * x_norm[1:]))
        
        # Add chaotic sinusoidal modulation with varying frequencies
        chaotic_mod = np.sum(np.sin(20 * x_norm + np.sin(5 * x_norm)) * 
                            np.cos(13 * x_norm + np.sin(9 * x_norm)))
        
        # Final multimodal landscape with chaotic basin structure
        return (np.sum(rbfs) + 0.5 * phase + 0.3 * poly_term + 
                0.2 * coupling + 0.15 * chaotic_mod)