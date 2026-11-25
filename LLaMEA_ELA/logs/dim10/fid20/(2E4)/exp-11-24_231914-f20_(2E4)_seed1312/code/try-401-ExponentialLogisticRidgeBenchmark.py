import numpy as np

class ExponentialLogisticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Exponential barrier parameters
        self.barrier_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.barrier_heights = np.random.uniform(2.0, 8.0, size=dim)
        self.barrier_widths = np.random.uniform(0.3, 1.5, size=dim)
        
        # Logistic map chaos parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, size=dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, size=dim)
        
        # Spectral decomposition components
        self.spectral_freqs = np.random.uniform(1.0, 6.0, size=dim)
        self.spectral_amps = np.random.uniform(0.5, 3.0, size=dim)
        self.spectral_phases = np.random.uniform(0.0, 2*np.pi, size=dim)
        
        # Ridge structure parameters
        self.ridge_directions = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        self.ridge_widths = np.random.uniform(0.5, 2.0, size=dim)
        self.ridge_heights = np.random.uniform(1.0, 4.0, size=dim)
        
        # Adaptive coupling weights
        self.coupling_strength = np.random.uniform(0.5, 2.5, size=dim)
        
        # Multi-scale exponential components
        self.exp_scales = np.random.uniform(0.5, 3.0, size=dim)
        self.exp_amplitudes = np.random.uniform(1.0, 5.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential barrier component
        barrier_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.barrier_centers[i])
            barrier_val = self.barrier_heights[i] * np.exp(-dist / self.barrier_widths[i])
            barrier_component += barrier_val
            
        # Logistic map chaos component
        chaos_component = 0.0
        for i in range(self.dim):
            # Update logistic map
            self.logistic_x[i] = self.logistic_r[i] * self.logistic_x[i] * (1 - self.logistic_x[i])
            chaos_val = self.logistic_x[i] * np.sin(x[i])
            chaos_component += chaos_val
            
        # Spectral decomposition component
        spectral_component = 0.0
        for i in range(self.dim):
            spec_val = self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i] + self.spectral_phases[i])
            spectral_component += spec_val
            
        # Ridge structure component
        ridge_component = 0.0
        for i in range(self.dim):
            ridge_val = 0.0
            for j in range(self.dim):
                ridge_val += self.ridge_directions[i, j] * x[j]
            ridge_val = np.exp(-0.5 * (ridge_val / self.ridge_widths[i]) ** 2)
            ridge_component += self.ridge_heights[i] * ridge_val
            
        # Adaptive coupling component
        coupling_component = 0.0
        for i in range(self.dim):
            coupling_val = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_val += (x[i] - x[j]) ** 2
            coupling_component += self.coupling_strength[i] * coupling_val
            
        # Multi-scale exponential component
        exp_component = 0.0
        for i in range(self.dim):
            exp_val = self.exp_amplitudes[i] * np.exp(-self.exp_scales[i] * np.abs(x[i]))
            exp_component += exp_val
            
        # Combine all components with appropriate weights
        return (1.2 * barrier_component + 
                1.0 * chaos_component + 
                0.8 * spectral_component + 
                0.9 * ridge_component + 
                0.7 * coupling_component + 
                0.6 * exp_component)