import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        centers = np.linspace(-1, 1, min(15, self.dim))
        if self.dim > 15:
            # Generate random centers for higher dimensions
            np.random.seed(42)
            centers = np.random.uniform(-1, 1, self.dim)
        
        # Radial basis with chaotic width modulation
        rbfs = []
        for i in range(min(15, self.dim)):
            center = centers[i] if self.dim <= 15 else np.random.uniform(-1, 1)
            sigma = 0.3 + 0.4 * np.sin(20 * center + np.pi/4)  # Enhanced chaotic width modulation
            rbfs.append(np.exp(-np.sum((x_norm - center)**2) / (2 * sigma**2)))
        
        # Add chaotic phase term for multimodality with exponential coupling
        phase = np.sum(np.sin(25 * x_norm + np.sin(13 * x_norm))**2)
        
        # Polynomial terms with chaotic coefficients
        poly_term = np.sum(0.8 * x_norm**6 + 0.4 * x_norm**5 - 0.6 * x_norm**4 + 0.2 * x_norm**3)
        
        # Chaotic coupling between dimensions with exponential scaling
        coupling = 0.5 * np.sum(np.exp(10 * np.sin(15 * x_norm[:-1])) * np.cos(12 * x_norm[1:]))
        
        # Add chaotic sinusoidal modulation with varying frequencies and dynamic amplitudes
        chaotic_mod = np.sum(np.sin(30 * x_norm + np.sin(17 * x_norm)) * 
                            np.cos(22 * x_norm + np.sin(19 * x_norm)) * 
                            (1 + 0.5 * np.sin(8 * x_norm)))
        
        # Add exponential basin structure for increased ruggedness
        basin_structure = np.sum(np.exp(-5 * np.abs(x_norm - np.mean(x_norm))) * 
                               np.sin(30 * x_norm)**2)
        
        # Final multimodal landscape with enhanced chaotic basin structure
        return (np.sum(rbfs) + 0.7 * phase + 0.4 * poly_term + 
                0.3 * coupling + 0.25 * chaotic_mod + 0.2 * basin_structure)