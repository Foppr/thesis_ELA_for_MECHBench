import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple scales and interaction terms
        exp_decay = np.sum(0.8 * np.exp(-x_norm**2) + 0.4 * np.exp(-2 * x_norm**2) + 0.2 * np.exp(-0.5 * x_norm**2) + 0.1 * np.exp(-3 * x_norm**2))
        
        # Higher frequency trigonometric terms with complex coupling
        trig1 = np.sum(np.sin(15 * x_norm) * np.cos(23 * x_norm) + 0.5 * np.sin(31 * x_norm) * np.cos(41 * x_norm))
        trig2 = np.sum(np.sin(37 * x_norm) * np.cos(53 * x_norm) + 0.3 * np.sin(67 * x_norm) * np.cos(79 * x_norm))
        trig3 = np.sum(np.sin(83 * x_norm) * np.cos(97 * x_norm) + 0.7 * np.sin(101 * x_norm) * np.cos(107 * x_norm))
        
        # Additional radial basis functions with varying widths and centers
        rbf1 = np.sum(np.exp(-8.0 * (x_norm - 0.2)**2) + 0.5 * np.exp(-6.0 * (x_norm - 0.7)**2))
        rbf2 = np.sum(np.exp(-4.0 * (x_norm + 0.4)**2) + 0.3 * np.exp(-5.0 * (x_norm + 0.9)**2))
        rbf3 = np.sum(np.exp(-9.0 * (x_norm - 0.6)**2) + 0.6 * np.exp(-7.0 * (x_norm - 0.3)**2))
        rbf4 = np.sum(np.exp(-10.0 * (x_norm + 0.1)**2) + 0.4 * np.exp(-8.0 * (x_norm + 0.8)**2))
        
        # Enhanced asymmetric gradient component with higher order terms
        asym_grad = np.sum(np.abs(x_norm)**4 * np.sign(x_norm) + 0.5 * np.abs(x_norm)**5 * np.sign(x_norm))
        
        # Novel chaotic component with multi-dimensional coupling and higher complexity
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(30 * x_norm[i] * x_norm[i+1]) * np.cos(25 * x_norm[i] * x_norm[i+1]) + \
                          0.5 * np.sin(40 * x_norm[i]**2 * x_norm[i+1]**2) * np.cos(35 * x_norm[i]**2 * x_norm[i+1]**2)
        
        # Stronger polynomial interaction terms with mixed exponents and cross-terms
        poly_interaction = np.sum(x_norm[:-1]**4 * x_norm[1:]**3 + x_norm[:-1]**3 * x_norm[1:]**4 + \
                                0.5 * x_norm[:-2]**2 * x_norm[1:-1]**3 * x_norm[2:]**2)
        
        # Mixed exponential and high-frequency trigonometric term
        mixed_exp_trig = np.sum(np.exp(-x_norm**2) * np.sin(15 * x_norm) + 0.3 * np.exp(-2 * x_norm**2) * np.cos(20 * x_norm))
        
        # Additional high-frequency chaotic component with multiple coupling
        high_freq = np.sum(np.sin(70 * x_norm) * np.cos(80 * x_norm) + 0.5 * np.sin(90 * x_norm) * np.cos(100 * x_norm))
        
        # Additional complex interaction between dimensions
        dim_interaction = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                dim_interaction += np.sin(10 * x_norm[i] * x_norm[i+1] * x_norm[i+2]) * np.cos(8 * x_norm[i] * x_norm[i+1] * x_norm[i+2])
        
        # New sine-cosine polynomial interaction term with increased complexity
        new_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                new_interaction += (np.sin(25 * x_norm[i]**2) * np.cos(35 * x_norm[i+1]**2) + 
                                  0.3 * np.sin(45 * x_norm[i] * x_norm[i+1]) * np.cos(55 * x_norm[i] * x_norm[i+1]) +
                                  0.2 * np.sin(65 * x_norm[i]**3) * np.cos(75 * x_norm[i+1]**3) +
                                  0.1 * np.sin(85 * x_norm[i] * x_norm[i+1]**2) * np.cos(95 * x_norm[i]**2 * x_norm[i+1]))
        
        # Additional higher-order polynomial coupling terms
        high_order_poly = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                high_order_poly += (x_norm[i]**5 * x_norm[i+1]**4 * x_norm[i+2]**3 + 
                                  0.5 * x_norm[i]**3 * x_norm[i+1]**5 * x_norm[i+2]**4)
        
        # Increased dimensional complexity with interaction between all dimensions
        full_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    full_interaction += np.sin(15 * x_norm[i] * x_norm[j]) * np.cos(20 * x_norm[i] * x_norm[j]) + \
                                      0.3 * np.sin(25 * x_norm[i]**2 * x_norm[j]**2) * np.cos(30 * x_norm[i]**2 * x_norm[j]**2)
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.3 * exp_decay + 
                0.25 * trig1 + 
                0.2 * trig2 + 
                0.15 * trig3 + 
                0.12 * rbf1 + 
                0.1 * rbf2 + 
                0.08 * rbf3 + 
                0.06 * rbf4 + 
                0.15 * asym_grad + 
                0.1 * chaotic + 
                0.08 * poly_interaction + 
                0.06 * mixed_exp_trig + 
                0.04 * high_freq + 
                0.03 * dim_interaction + 
                0.05 * new_interaction + 
                0.02 * high_order_poly + 
                0.01 * full_interaction + 
                noise)