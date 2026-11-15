import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay base with varying scales
        exp_decay = np.sum(np.exp(-x_norm**2) + 0.5 * np.exp(-2 * x_norm**2) + 0.3 * np.exp(-0.5 * x_norm**2))
        
        # Trigonometric terms with varying frequencies and amplitudes
        trig1 = np.sum(np.sin(7 * x_norm) * np.cos(13 * x_norm))
        trig2 = np.sum(np.sin(11 * x_norm) * np.cos(19 * x_norm))
        trig3 = np.sum(np.sin(23 * x_norm) * np.cos(31 * x_norm))
        
        # Radial basis functions with different widths and centers
        rbf1 = np.sum(np.exp(-5.0 * (x_norm - 0.3)**2))
        rbf2 = np.sum(np.exp(-3.0 * (x_norm + 0.5)**2))
        rbf3 = np.sum(np.exp(-7.0 * (x_norm - 0.8)**2))
        
        # Asymmetric gradient component creating non-uniform valleys
        asym_grad = np.sum(np.abs(x_norm)**3 * np.sign(x_norm))
        
        # Chaotic sine-wave component with coupling between dimensions
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(20 * x_norm[i] * x_norm[i+1]) * np.cos(15 * x_norm[i] * x_norm[i+1])
        
        # Polynomial interaction terms with mixed exponents
        poly_interaction = np.sum(x_norm[:-1]**3 * x_norm[1:]**2 + x_norm[:-1]**2 * x_norm[1:]**3)
        
        # Mixed exponential and trigonometric term
        mixed_exp_trig = np.sum(np.exp(-x_norm**2) * np.sin(9 * x_norm))
        
        # Additional high-frequency chaotic component
        high_freq = np.sum(np.sin(50 * x_norm) * np.cos(60 * x_norm))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * exp_decay + 
                0.2 * trig1 + 
                0.15 * trig2 + 
                0.1 * trig3 + 
                0.1 * rbf1 + 
                0.08 * rbf2 + 
                0.06 * rbf3 + 
                0.1 * asym_grad + 
                0.05 * chaotic + 
                0.04 * poly_interaction + 
                0.03 * mixed_exp_trig + 
                0.02 * high_freq + 
                noise)