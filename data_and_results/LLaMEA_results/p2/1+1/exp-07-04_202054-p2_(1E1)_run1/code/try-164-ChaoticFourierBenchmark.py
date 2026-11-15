import numpy as np

class ChaoticFourierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.freqs = np.random.uniform(1.0, 10.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize with quadratic base
        f_value = np.sum(x**2) * 0.1
        
        # Add chaotic logistic map components
        logistic_vals = np.zeros(self.dim)
        for i in range(self.dim):
            # Simple logistic map iteration
            val = 0.5
            for _ in range(10):
                val = self.r_values[i] * val * (1 - val)
            logistic_vals[i] = val
            
        f_value += 0.5 * np.sum(logistic_vals * np.sin(x))
        
        # Add Fourier series components with chaotic frequencies
        for i in range(self.dim):
            f_value += self.amps[i] * np.sin(self.freqs[i] * x[i] + logistic_vals[i] * np.pi/4)
            
        # Add multi-scale harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                f_value += 0.3 * np.sin(self.freqs[i] * x[i] + self.freqs[j] * x[j]) * \
                          np.cos(logistic_vals[i] * x[j] + logistic_vals[j] * x[i])
                
        # Add chaotic phase modulation
        phase_mod = np.zeros(self.dim)
        for i in range(self.dim):
            phase_mod[i] = np.sin(logistic_vals[i] * 10) * np.cos(logistic_vals[i] * 15)
            
        f_value += 0.4 * np.sum(phase_mod * x**2)
        
        # Add polynomial chaos with logistic modulation
        for i in range(self.dim):
            f_value += 0.2 * x[i]**5 * (1 + logistic_vals[i] * np.sin(x[i]))
            
        # Add saddle point structure via cross terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.sin(x[i] * x[j]) * np.cos(logistic_vals[i] + logistic_vals[j])
                
        # Add irregular high-frequency component
        f_value += 0.3 * np.sum(np.sin(20 * x + logistic_vals * np.pi/3) * np.cos(15 * x))
        
        # Add noise-like irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.05 * np.sum(noise * np.sin(x))
        
        return f_value