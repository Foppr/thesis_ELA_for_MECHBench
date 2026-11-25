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
            trig_term += np.sin(3.5 * np.pi * x_scaled[i]) * np.cos(4.5 * np.pi * x_scaled[i]) + \
                        0.6 * np.sin(7.2 * np.pi * x_scaled[i]) * np.cos(1.8 * np.pi * x_scaled[i])
        
        # Enhanced cross-dimensional interaction terms with higher-order products
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(1.2 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(2.8 * x_scaled[i] + 1.5 * x_scaled[j]) + 
                              0.4 * np.sin(1.8 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(0.7 * x_scaled[i] + 2.3 * x_scaled[j]))
        
        # Modified multimodal component with stronger local minima
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += (np.sin(14.5 * x_scaled[i]) * np.exp(-x_scaled[i]**2) + 
                          0.8 * np.sin(7.8 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/2))
        
        # Additional harmonic term to increase landscape complexity
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += np.sin(3.8 * np.pi * x_scaled[i])**2 + 0.6 * np.cos(5.7 * np.pi * x_scaled[i])**2
        
        # Combine all terms with optimized weights
        return -0.55 * exp_term + 0.45 * trig_term + 0.35 * cross_term + 0.55 * multi_term + 0.25 * harm_term + 2.6