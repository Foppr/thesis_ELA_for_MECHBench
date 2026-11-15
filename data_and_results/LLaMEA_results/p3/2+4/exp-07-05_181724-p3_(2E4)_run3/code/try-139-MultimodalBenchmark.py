import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple scales and interaction terms
        exp_decay = np.sum(0.9 * np.exp(-x_norm**2) + 0.5 * np.exp(-2 * x_norm**2) + 0.3 * np.exp(-0.5 * x_norm**2) + 0.15 * np.exp(-3 * x_norm**2))
        
        # Higher frequency trigonometric terms with complex coupling
        trig1 = np.sum(np.sin(20 * x_norm) * np.cos(30 * x_norm) + 0.6 * np.sin(40 * x_norm) * np.cos(50 * x_norm))
        trig2 = np.sum(np.sin(45 * x_norm) * np.cos(60 * x_norm) + 0.4 * np.sin(70 * x_norm) * np.cos(80 * x_norm))
        trig3 = np.sum(np.sin(85 * x_norm) * np.cos(100 * x_norm) + 0.8 * np.sin(110 * x_norm) * np.cos(120 * x_norm))
        
        # Additional radial basis functions with varying widths and centers
        rbf1 = np.sum(np.exp(-10.0 * (x_norm - 0.2)**2) + 0.6 * np.exp(-7.0 * (x_norm - 0.7)**2))
        rbf2 = np.sum(np.exp(-5.0 * (x_norm + 0.4)**2) + 0.4 * np.exp(-6.0 * (x_norm + 0.9)**2))
        rbf3 = np.sum(np.exp(-11.0 * (x_norm - 0.6)**2) + 0.7 * np.exp(-8.0 * (x_norm - 0.3)**2))
        rbf4 = np.sum(np.exp(-12.0 * (x_norm + 0.1)**2) + 0.5 * np.exp(-9.0 * (x_norm + 0.8)**2))
        
        # Enhanced asymmetric gradient component with higher order terms
        asym_grad = np.sum(np.abs(x_norm)**5 * np.sign(x_norm) + 0.6 * np.abs(x_norm)**6 * np.sign(x_norm))
        
        # Novel chaotic component with multi-dimensional coupling and higher complexity
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(40 * x_norm[i] * x_norm[i+1]) * np.cos(35 * x_norm[i] * x_norm[i+1]) + \
                          0.6 * np.sin(50 * x_norm[i]**2 * x_norm[i+1]**2) * np.cos(45 * x_norm[i]**2 * x_norm[i+1]**2)
        
        # Stronger polynomial interaction terms with mixed exponents and cross-terms
        poly_interaction = np.sum(x_norm[:-1]**5 * x_norm[1:]**4 + x_norm[:-1]**4 * x_norm[1:]**5 + \
                                0.6 * x_norm[:-2]**3 * x_norm[1:-1]**4 * x_norm[2:]**3)
        
        # Mixed exponential and high-frequency trigonometric term
        mixed_exp_trig = np.sum(np.exp(-x_norm**2) * np.sin(20 * x_norm) + 0.4 * np.exp(-2 * x_norm**2) * np.cos(25 * x_norm))
        
        # Additional high-frequency chaotic component with multiple coupling
        high_freq = np.sum(np.sin(80 * x_norm) * np.cos(90 * x_norm) + 0.6 * np.sin(100 * x_norm) * np.cos(110 * x_norm))
        
        # Additional complex interaction between dimensions
        dim_interaction = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                dim_interaction += np.sin(15 * x_norm[i] * x_norm[i+1] * x_norm[i+2]) * np.cos(10 * x_norm[i] * x_norm[i+1] * x_norm[i+2])
        
        # New sine-cosine polynomial interaction term with increased complexity
        new_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                new_interaction += (np.sin(30 * x_norm[i]**2) * np.cos(40 * x_norm[i+1]**2) + 
                                  0.4 * np.sin(50 * x_norm[i] * x_norm[i+1]) * np.cos(60 * x_norm[i] * x_norm[i+1]) +
                                  0.3 * np.sin(70 * x_norm[i]**3) * np.cos(80 * x_norm[i+1]**3))
        
        # Additional higher-order chaotic interaction
        high_order_chaos = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                high_order_chaos += np.sin(20 * x_norm[i]**2 * x_norm[i+1] * x_norm[i+2]) * np.cos(15 * x_norm[i] * x_norm[i+1]**2 * x_norm[i+2])
        
        # Increased dimensionality-dependent complexity multiplier
        dim_multiplier = 1.0 + 0.15 * (self.dim - 1)
        
        # Add noise for non-triviality
        noise = 0.0015 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.35 * exp_decay * dim_multiplier + 
                0.3 * trig1 * dim_multiplier + 
                0.25 * trig2 * dim_multiplier + 
                0.2 * trig3 * dim_multiplier + 
                0.15 * rbf1 * dim_multiplier + 
                0.12 * rbf2 * dim_multiplier + 
                0.1 * rbf3 * dim_multiplier + 
                0.08 * rbf4 * dim_multiplier + 
                0.18 * asym_grad * dim_multiplier + 
                0.15 * chaotic * dim_multiplier + 
                0.1 * poly_interaction * dim_multiplier + 
                0.08 * mixed_exp_trig * dim_multiplier + 
                0.06 * high_freq * dim_multiplier + 
                0.04 * dim_interaction * dim_multiplier + 
                0.06 * new_interaction * dim_multiplier + 
                0.03 * high_order_chaos * dim_multiplier + 
                noise)