import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric quadratic terms with varying curvature
        quad_term = np.sum(0.5 * x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)
        
        # Multi-modal component with multiple local minima and saddle points
        modal_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) + 
                           0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Saddle point structure with gradient reversal
        saddle_term = np.sum(x_scaled * np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Gradient variability through non-uniform exponential decay
        exp_term = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * np.sin(2 * x_scaled))
        
        # Implicit constraint term that penalizes regions far from optimal paths
        constraint_term = np.sum((x_scaled**2 - 1)**2 * (x_scaled**2 - 4)**2)
        
        # Asymmetric high-frequency modulation with varying amplitudes
        freq_term = np.sum(0.7 * np.sin(10 * x_scaled) * np.cos(8 * x_scaled) + 
                          0.3 * np.sin(15 * x_scaled) * np.cos(12 * x_scaled))
        
        # Combine all terms with different weights
        return 0.4 * quad_term + 0.3 * modal_term + 0.15 * saddle_term + 0.05 * exp_term + 0.05 * constraint_term + 0.05 * freq_term + 2.0