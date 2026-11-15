import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with mixed degrees
        poly_chaos = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**5 + 0.4 * x_norm**4 + 0.2 * x_norm**3)
        
        # Radial basis functions with varying widths and centers
        rbf1 = np.sum(np.exp(-15.0 * (x_norm - 0.3)**2) + 0.6 * np.exp(-12.0 * (x_norm - 0.7)**2))
        rbf2 = np.sum(np.exp(-10.0 * (x_norm + 0.4)**2) + 0.4 * np.exp(-8.0 * (x_norm + 0.8)**2))
        rbf3 = np.sum(np.exp(-20.0 * (x_norm - 0.1)**2) + 0.7 * np.exp(-18.0 * (x_norm - 0.6)**2))
        
        # Sine-cosine polynomial interaction terms
        trig_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                trig_interaction += (np.sin(20 * x_norm[i]) * np.cos(25 * x_norm[i+1]) + 
                                  0.5 * np.sin(30 * x_norm[i+1]) * np.cos(35 * x_norm[i]) + 
                                  0.3 * np.sin(40 * x_norm[i]**2) * np.cos(45 * x_norm[i+1]**2))
        
        # Cross-dimensional polynomial interactions with mixed exponents
        cross_poly = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                cross_poly += (x_norm[i]**3 * x_norm[i+1]**2 * x_norm[i+2]**1 + 
                             0.5 * x_norm[i]**2 * x_norm[i+1]**3 * x_norm[i+2]**2 + 
                             0.3 * x_norm[i]**1 * x_norm[i+1]**2 * x_norm[i+2]**3)
        
        # Asymmetric exponential terms with different decay rates
        asym_exp = np.sum(0.8 * np.exp(-3.0 * np.abs(x_norm)) + 0.4 * np.exp(-5.0 * np.abs(x_norm)) + 
                         0.2 * np.exp(-7.0 * np.abs(x_norm)))
        
        # Higher-order trigonometric terms with multiple frequencies
        high_trig = np.sum(np.sin(50 * x_norm) + 0.7 * np.sin(60 * x_norm) + 0.5 * np.sin(70 * x_norm) + 
                          0.3 * np.sin(80 * x_norm) + 0.1 * np.sin(90 * x_norm))
        
        # Chaotic sine-cosine coupling between dimensions
        chaotic_coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_coupling += np.sin(35 * x_norm[i] * x_norm[i+1] + 0.5 * np.cos(45 * x_norm[i] * x_norm[i+1]))
        
        # Non-separable polynomial interaction with mixed cross-terms
        non_sep_poly = np.sum(x_norm[:-1]**2 * x_norm[1:]**3 + x_norm[:-1]**3 * x_norm[1:]**2 + 
                             0.5 * x_norm[:-2]**2 * x_norm[1:-1]**2 * x_norm[2:]**1)
        
        # Additional complex interaction using combined exponential and trigonometric terms
        exp_trig_combo = np.sum(np.exp(-x_norm**2) * np.sin(25 * x_norm) + 0.3 * np.exp(-2 * x_norm**2) * np.cos(30 * x_norm))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.2 * poly_chaos + 
                0.15 * rbf1 + 
                0.12 * rbf2 + 
                0.1 * rbf3 + 
                0.08 * trig_interaction + 
                0.07 * cross_poly + 
                0.06 * asym_exp + 
                0.05 * high_trig + 
                0.04 * chaotic_coupling + 
                0.03 * non_sep_poly + 
                0.02 * exp_trig_combo + 
                noise)