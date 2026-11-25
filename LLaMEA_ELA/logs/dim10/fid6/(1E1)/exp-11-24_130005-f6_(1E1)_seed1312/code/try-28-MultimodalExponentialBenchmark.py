import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential potential wells with varying decay rates
        exp_term = np.sum(np.exp(-2.0 * x_scaled**2) + 0.5 * np.exp(-0.5 * x_scaled**2))
        
        # Highly complex trigonometric oscillations with non-uniform frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += (np.sin(5.0 * np.pi * x_scaled[i]) * np.cos(6.5 * np.pi * x_scaled[i]) + 
                         0.7 * np.sin(12.3 * np.pi * x_scaled[i]) * np.cos(2.1 * np.pi * x_scaled[i]) +
                         0.4 * np.sin(9.8 * np.pi * x_scaled[i]) * np.cos(3.7 * np.pi * x_scaled[i]))
        
        # Stronger cross-dimensional interaction with polynomial coupling terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(2.5 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(3.2 * x_scaled[i] + 2.8 * x_scaled[j]) + 
                              0.6 * np.sin(1.7 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(1.3 * x_scaled[i] + 3.9 * x_scaled[j]) +
                              0.3 * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(4.0 * x_scaled[i] * x_scaled[j]))
        
        # Augmented multimodal component with multiple local minima and saddle points
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += (np.sin(18.2 * x_scaled[i]) * np.exp(-x_scaled[i]**2) + 
                          0.9 * np.sin(11.7 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/3) +
                          0.5 * np.sin(6.4 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/0.5))
        
        # Additional complex harmonic terms with varying phase shifts
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += (np.sin(4.2 * np.pi * x_scaled[i])**3 + 0.7 * np.cos(6.9 * np.pi * x_scaled[i])**3 +
                         0.3 * np.sin(8.1 * np.pi * x_scaled[i])**2 + 0.5 * np.cos(5.3 * np.pi * x_scaled[i])**2)
        
        # Novel interaction term with higher-order cross-dimensional products
        high_order_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    high_order_term += np.sin(1.5 * x_scaled[i] * x_scaled[j] * x_scaled[k]) * \
                                      np.cos(2.3 * x_scaled[i] + 1.8 * x_scaled[j] + 3.1 * x_scaled[k])
        
        # Combine all terms with optimized weights
        return -0.65 * exp_term + 0.55 * trig_term + 0.45 * cross_term + 0.65 * multi_term + 0.35 * harm_term + 0.25 * high_order_term + 3.1