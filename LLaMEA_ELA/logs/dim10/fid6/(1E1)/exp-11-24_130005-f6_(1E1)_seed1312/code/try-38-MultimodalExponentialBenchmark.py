import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay term that encourages convergence to center
        exp_term = np.sum(np.exp(-x_scaled**2))
        
        # Enhanced trigonometric oscillations with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(4.0 * np.pi * x_scaled[i]) * np.cos(5.0 * np.pi * x_scaled[i]) + \
                        0.7 * np.sin(8.0 * np.pi * x_scaled[i]) * np.cos(2.0 * np.pi * x_scaled[i])
        
        # Enhanced cross-dimensional interaction terms with higher-order products
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(1.5 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(3.0 * x_scaled[i] + 2.0 * x_scaled[j]) + 
                              0.5 * np.sin(2.0 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(1.0 * x_scaled[i] + 3.0 * x_scaled[j]))
        
        # Modified multimodal component with stronger local minima
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += (np.sin(15.0 * x_scaled[i]) * np.exp(-x_scaled[i]**2) + 
                          0.9 * np.sin(8.0 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/2))
        
        # Additional harmonic term to increase landscape complexity
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += np.sin(4.0 * np.pi * x_scaled[i])**2 + 0.7 * np.cos(6.0 * np.pi * x_scaled[i])**2
        
        # Combine all terms with optimized weights
        return -0.6 * exp_term + 0.5 * trig_term + 0.4 * cross_term + 0.6 * multi_term + 0.3 * harm_term + 2.7