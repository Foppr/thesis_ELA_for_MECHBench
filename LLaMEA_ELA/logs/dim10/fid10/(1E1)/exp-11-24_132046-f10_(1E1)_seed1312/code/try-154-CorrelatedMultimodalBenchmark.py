import numpy as np

class CorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal component with chaotic sine modulation and heavy-tailed decay
        f1 = np.sum(np.exp(-0.7 * np.abs(x_norm)) * (1 + 0.6 * np.sin(15 * x_norm) * np.cos(13 * x_norm)))
        
        # Fractal-like power-law correlation with stochastic perturbations
        f2 = np.sum((1 + 0.4 * np.sin(20 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)**1.7) * 
                   (1 + 0.3 * np.cos(18 * x_norm) * np.sin(16 * x_norm)))
        
        # Multi-scale oscillatory pattern with varying frequency and amplitude
        f3 = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                   (1 + 0.4 * np.sin(20 * x_norm)) * 
                   (1 + 0.3 * np.cos(17 * x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)))
        
        # Basin structure with non-smooth curvature and exponential scaling
        f4 = np.sum(np.exp(-x_norm**2.5) * 
                   (1 + 0.5 * np.sin(20 * x_norm)) * 
                   (1 + 0.4 * np.cos(18 * x_norm)) * 
                   (1 + 0.3 * np.sin(16 * x_norm)) * 
                   (1 + 0.2 * np.cos(14 * x_norm)))
        
        # Cross-dimensional interactions with long-range dependencies and memory effects
        f5 = np.sum(np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])**1.5) * 
                   (1 + 0.3 * np.sin(8 * x_norm[:-1])) * 
                   (1 + 0.2 * np.cos(7 * x_norm[1:])) * 
                   (1 + 0.1 * np.sin(6 * x_norm[:-1])) * 
                   (1 + 0.05 * np.cos(5 * x_norm[1:])))
        
        # Variable scaling with heavy-tailed power-law behavior and stochastic modulation
        f6 = np.sum(np.abs(x_norm)**2.3 * 
                   (1 + 0.5 * np.sin(18 * x_norm)) * 
                   (1 + 0.4 * np.cos(16 * x_norm)) * 
                   (1 + 0.3 * np.sin(14 * x_norm)) * 
                   (1 + 0.2 * np.cos(12 * x_norm)))
        
        # Memory effect with delayed fractal correlation structure and chaotic modulation
        f7 = np.sum(np.exp(-0.5 * np.abs(x_norm)**1.8) * 
                   (1 + 0.4 * np.sin(19 * x_norm)) * 
                   (1 + 0.3 * np.cos(17 * x_norm)) * 
                   (1 + 0.2 * np.sin(15 * x_norm)) * 
                   (1 + 0.1 * np.cos(13 * x_norm)))
        
        # Adaptive amplitude modulation with chaotic decay and multi-scale oscillations
        f8 = np.sum(np.exp(-0.3 * x_norm**2.2) * 
                   (1 + 0.6 * np.sin(22 * x_norm)) * 
                   (1 + 0.5 * np.cos(20 * x_norm)) * 
                   (1 + 0.4 * np.sin(18 * x_norm)) * 
                   (1 + 0.3 * np.cos(16 * x_norm)) * 
                   (1 + 0.2 * np.sin(14 * x_norm)))
        
        # Combined global structure with fractal interactions and non-separable correlations
        f9 = np.sum(np.exp(-0.4 * np.abs(x_norm)**1.9) * 
                    (1 + 0.3 * np.sin(21 * x_norm)) * 
                    (1 + 0.4 * np.cos(19 * x_norm)) * 
                    (1 + 0.2 * np.sin(17 * x_norm)) * 
                    (1 + 0.1 * np.cos(15 * x_norm)) * 
                    (1 + 0.05 * np.sin(13 * x_norm)))
        
        # Add non-linear dimension coupling with chaotic cross-interactions
        f10 = np.sum(np.exp(-0.35 * np.abs(x_norm[:-1] - x_norm[1:])**2) * 
                     (1 + 0.3 * np.sin(9 * x_norm[:-1])) * 
                     (1 + 0.25 * np.cos(8 * x_norm[1:])) * 
                     (1 + 0.2 * np.sin(7 * x_norm[:-1])) * 
                     (1 + 0.15 * np.cos(6 * x_norm[1:])))
        
        # Enhanced global scaling with exponential and power-law combined
        f11 = np.sum(np.abs(x_norm)**2.1 * 
                     (1 + 0.4 * np.sin(19 * x_norm)) * 
                     (1 + 0.3 * np.cos(17 * x_norm)) * 
                     (1 + 0.2 * np.sin(15 * x_norm)) * 
                     (1 + 0.1 * np.cos(13 * x_norm)))
        
        # Return combined fitness with increased complexity and chaotic behavior
        return 2.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)