import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component with modified frequencies
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) + np.cos(2 * np.pi * x_scaled))
        
        # Exponential decay component with altered decay rate
        exp_term = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * np.sin(4 * x_scaled))
        
        # Enhanced polynomial term with modified coefficients and higher degree interactions
        poly_term = np.sum(0.5 * x_scaled**6 + 0.4 * x_scaled**4 + 0.6 * x_scaled**2)
        
        # Chaotic component with increased nonlinearity
        chaotic_term = np.sum(np.sin(x_scaled**3) * np.cos(x_scaled) + 0.3 * np.sin(5 * x_scaled) * np.cos(3 * x_scaled))
        
        # Additional interaction term between dimensions with shifted indices
        interaction_term = np.sum(np.sin(x_scaled[:-2] - x_scaled[2:]) * np.cos(x_scaled[:-2] + x_scaled[2:]))
        
        # Combine all terms with updated weights
        return 0.3 * trig_term + 0.25 * exp_term + 0.3 * poly_term + 0.1 * chaotic_term + 0.05 * interaction_term + 1.5