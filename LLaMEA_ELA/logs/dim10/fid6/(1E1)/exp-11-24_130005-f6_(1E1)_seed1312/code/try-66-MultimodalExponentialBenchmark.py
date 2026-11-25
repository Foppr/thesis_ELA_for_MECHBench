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
            freq1 = 4.0 + 0.4 * np.sin(2.5 * x_scaled[i])
            freq2 = 5.0 + 0.3 * np.cos(2.0 * x_scaled[i])
            trig_term += np.sin(freq1 * np.pi * x_scaled[i]) * np.cos(freq2 * np.pi * x_scaled[i]) + \
                        0.7 * np.sin(8.0 * np.pi * x_scaled[i]) * np.cos(2.0 * np.pi * x_scaled[i])
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.5 + 0.3 * np.sin(3.5 * x_scaled[i] + 3.0 * x_scaled[j])
                cross_term += (np.sin(coupling * 1.5 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(3.0 * x_scaled[i] + 2.0 * x_scaled[j]) + 
                              0.5 * np.sin(2.0 * x_scaled[i] * x_scaled[j]) * 
                              np.cos(1.0 * x_scaled[i] + 2.5 * x_scaled[j]))
        
        # Modified multimodal component with nested local minima and chaotic modulation
        multi_term = 0.0
        for i in range(self.dim):
            mod_freq = 16.0 + 2.5 * np.sin(3.5 * x_scaled[i])
            multi_term += (np.sin(mod_freq * x_scaled[i]) * np.exp(-x_scaled[i]**2) + 
                          0.9 * np.sin(8.5 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/2) + 
                          0.4 * np.sin(28.0 * x_scaled[i]) * np.exp(-(x_scaled[i]**2)/3))
        
        # Additional harmonic term with nested frequencies to increase landscape complexity
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += (np.sin(4.0 * np.pi * x_scaled[i])**2 + 
                         0.7 * np.cos(6.0 * np.pi * x_scaled[i])**2 + 
                         0.5 * np.sin(10.0 * np.pi * x_scaled[i])**3)
        
        # Chaotic modulation term for increased difficulty
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(14.0 * x_scaled[i]) * np.cos(9.0 * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Combine all terms with optimized weights (slightly modified)
        return -0.6 * exp_term + 0.5 * trig_term + 0.4 * cross_term + 0.6 * multi_term + 0.3 * harm_term + 0.35 * chaos_term + 2.7