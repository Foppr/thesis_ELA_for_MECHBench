import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay term that encourages convergence to center
        exp_term = np.sum(np.exp(-x_scaled**2))
        
        # Enhanced trigonometric oscillations with varying frequencies and chaotic modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq1 = 3.5 + 0.3 * np.sin(2.2 * x_scaled[i])
            freq2 = 4.5 + 0.2 * np.cos(1.8 * x_scaled[i])
            trig_term += np.sin(freq1 * np.pi * x_scaled[i]) * np.cos(freq2 * np.pi * x_scaled[i]) + \
                        0.6 * np.sin(7.2 * np.pi * x_scaled[i]) * np.cos(1.8 * np.pi * x_scaled[i])
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.2 * np.sin(3.1 * x_scaled[i] + 2.7 * x_scaled[j])
                cross_term += (np.sin(coupling * 1.2 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(2.8 * x_scaled[i] + 1.5 * x_scaled[j]) + 
                              0.4 * np.sin(1.8 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(0.7 * x_scaled[i] + 2.3 * x_scaled[j]))
        
        # Modified multimodal component with nested local minima and chaotic modulation
        multi_term = 0.0
        for i in range(self.dim):
            mod_freq = 14.5 + 2.0 * np.sin(3.3 * x_scaled[i])
            multi_term += (np.sin(mod_freq * x_scaled[i]) * np.exp(-x_scaled[i]**2) + 
                          0.8 * np.sin(7.8 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/2) + 
                          0.3 * np.sin(25.1 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/3))
        
        # Additional harmonic term with nested frequencies to increase landscape complexity
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += (np.sin(3.8 * np.pi * x_scaled[i])**2 + 
                         0.6 * np.cos(5.7 * np.pi * x_scaled[i])**2 + 
                         0.4 * np.sin(9.1 * np.pi * x_scaled[i])**3)
        
        # Chaotic modulation term for increased difficulty
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(12.7 * x_scaled[i]) * np.cos(8.3 * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Combine all terms with optimized weights (slightly modified)
        return -0.57 * exp_term + 0.47 * trig_term + 0.37 * cross_term + 0.57 * multi_term + 0.27 * harm_term + 0.32 * chaos_term + 2.6