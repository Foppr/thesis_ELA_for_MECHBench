import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple scales and coupling
        exp_decay = np.sum(0.8 * np.exp(-x_norm**2) + 0.4 * np.exp(-3 * x_norm**2) + 0.2 * np.exp(-0.3 * x_norm**2) + 0.1 * np.exp(-5 * x_norm**2))
        
        # Higher frequency trigonometric terms with phase shifts
        trig1 = np.sum(np.sin(15 * x_norm) * np.cos(23 * x_norm) + 0.5 * np.sin(31 * x_norm) * np.cos(41 * x_norm))
        trig2 = np.sum(np.sin(37 * x_norm) * np.cos(53 * x_norm) + 0.3 * np.sin(67 * x_norm) * np.cos(79 * x_norm))
        trig3 = np.sum(np.sin(83 * x_norm) * np.cos(97 * x_norm) + 0.7 * np.sin(101 * x_norm) * np.cos(107 * x_norm))
        
        # Additional radial basis functions with varying widths and centers
        rbf1 = np.sum(np.exp(-8.0 * (x_norm - 0.2)**2) + 0.5 * np.exp(-4.0 * (x_norm - 0.7)**2))
        rbf2 = np.sum(np.exp(-6.0 * (x_norm + 0.4)**2) + 0.3 * np.exp(-2.0 * (x_norm + 0.9)**2))
        rbf3 = np.sum(np.exp(-10.0 * (x_norm - 0.6)**2) + 0.8 * np.exp(-3.0 * (x_norm - 0.1)**2))
        rbf4 = np.sum(np.exp(-5.0 * (x_norm + 0.3)**2) + 0.6 * np.exp(-7.0 * (x_norm + 0.8)**2))
        
        # Enhanced asymmetric gradient component with higher order terms
        asym_grad = np.sum(np.abs(x_norm)**4 * np.sign(x_norm) + 0.5 * np.abs(x_norm)**5 * np.sign(x_norm))
        
        # Novel chaotic sine-wave component with coupling between dimensions and time-like dependency
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(30 * x_norm[i] * x_norm[i+1] + 0.5 * np.sin(17 * x_norm[i])) * np.cos(25 * x_norm[i] * x_norm[i+1] + 0.3 * np.cos(13 * x_norm[i+1]))
        
        # Stronger polynomial interaction terms with mixed exponents and cross-terms
        poly_interaction = np.sum(x_norm[:-1]**4 * x_norm[1:]**3 + x_norm[:-1]**3 * x_norm[1:]**4 + 0.5 * x_norm[:-1]**5 * x_norm[1:]**2)
        
        # Mixed exponential and trigonometric term with higher frequencies
        mixed_exp_trig = np.sum(np.exp(-x_norm**2) * np.sin(13 * x_norm) + 0.3 * np.exp(-2 * x_norm**2) * np.cos(23 * x_norm))
        
        # Additional high-frequency chaotic component with multiple harmonics
        high_freq = np.sum(np.sin(80 * x_norm) * np.cos(90 * x_norm) + 0.5 * np.sin(100 * x_norm) * np.cos(110 * x_norm))
        
        # Additional noise and perturbation terms
        noise = 0.001 * np.random.random()
        perturbation = 0.0005 * np.sum(np.sin(100 * x_norm) + np.cos(120 * x_norm))
        
        # Combine all components with carefully tuned weights
        return (0.3 * exp_decay + 
                0.25 * trig1 + 
                0.2 * trig2 + 
                0.15 * trig3 + 
                0.12 * rbf1 + 
                0.1 * rbf2 + 
                0.08 * rbf3 + 
                0.06 * rbf4 + 
                0.1 * asym_grad + 
                0.07 * chaotic + 
                0.06 * poly_interaction + 
                0.05 * mixed_exp_trig + 
                0.03 * high_freq + 
                0.01 * noise + 
                0.01 * perturbation)