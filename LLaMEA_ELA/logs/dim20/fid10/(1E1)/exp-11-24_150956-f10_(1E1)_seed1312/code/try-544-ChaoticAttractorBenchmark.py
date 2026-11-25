import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function clusters with chaotic variance
        rbf_terms = np.sum(1.5 * np.exp(-2.0 * (x_scaled - 0.2)**2) + 
                          1.0 * np.exp(-3.0 * (x_scaled + 0.3)**2) + 
                          0.8 * np.exp(-1.5 * (x_scaled - 0.7)**2) + 
                          0.6 * np.exp(-4.0 * (x_scaled + 0.8)**2))
        
        # Chaotic sine-wave interference with logistic map modulation
        chaotic_sin = np.sum(np.sin(10.0 * x_scaled * (1.0 + 0.3 * np.sin(7.0 * x_scaled))) + 
                           0.7 * np.sin(15.0 * x_scaled**2 * (1.0 + 0.2 * np.cos(9.0 * x_scaled))) + 
                           0.5 * np.sin(20.0 * x_scaled**3 * (1.0 + 0.4 * np.sin(11.0 * x_scaled))))
        
        # Gradient-based attraction wells with exponential repulsion
        well_terms = np.sum(np.exp(-0.5 * (x_scaled - 0.1)**2) * np.cos(8.0 * x_scaled) + 
                          np.exp(-0.3 * (x_scaled + 0.5)**2) * np.sin(6.0 * x_scaled) + 
                          np.exp(-0.7 * (x_scaled - 0.9)**2) * np.cos(12.0 * x_scaled))
        
        # Cross-dimensional coupling with fractional polynomial interactions
        cross_dim = np.sum((x_scaled[:-1]**1.5 + x_scaled[1:]**1.5) * 
                          np.sin(4.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                          (x_scaled[:-2]**2.5 + x_scaled[2:]**2.5) * 
                          np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric landscape with piecewise polynomial behavior
        asym_term = np.sum(np.where(x_scaled < 0, 0.4 * x_scaled**3, 0.6 * x_scaled**4) + 
                         0.3 * np.abs(x_scaled)**2.2)
        
        # Final combined function with dynamic weighting
        return 0.4 * rbf_terms + 0.35 * chaotic_sin + 0.15 * well_terms + 0.08 * cross_dim + 0.02 * asym_term + 1.8