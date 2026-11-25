import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired interference patterns with complex amplitudes
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex phase coupling with exponential decay
                phase = np.sin(x[i]) * np.cos(x[j]) + np.cos(0.5 * x[i]) * np.sin(0.7 * x[j])
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * np.cos(phase)
                interference += coupling
        
        # Radial basis function cascade with multi-scale Gaussians
        rbf_cascade = 0
        for i in range(self.dim):
            # Multi-scale radial basis functions with varying widths and centers
            scale = 1.0 + 0.5 * np.sin(0.3 * x[i])
            width = 0.2 + 0.3 * np.cos(0.4 * x[i])
            center = 1.5 * np.sin(0.6 * x[i]) + 0.8 * np.cos(0.9 * x[i])
            rbf_cascade += scale * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Time-varying harmonic couplings with dynamic frequencies
        time_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic frequency modulation based on coordinates
                freq_i = 1.0 + 0.2 * np.sin(0.5 * x[i])
                freq_j = 1.0 + 0.3 * np.cos(0.4 * x[j])
                time_coupling += np.sin(freq_i * x[i] + freq_j * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Fractal-like oscillatory structure with diminishing amplitudes
        fractal_osc = 0
        for i in range(self.dim):
            # Oscillatory terms with decreasing amplitude based on dimension
            amp = 1.0 / (1.0 + 0.1 * i)
            freq = 2.0 + 0.5 * np.sin(0.3 * x[i])
            fractal_osc += amp * np.sin(freq * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Asymmetric exponential landscape with cross-dimensional interactions
        exp_landscape = 0
        for i in range(self.dim):
            # Exponential terms with asymmetric scaling
            asym_factor = 1.0 + 0.3 * np.sin(0.4 * x[i])
            exp_landscape += asym_factor * np.exp(-0.5 * x[i]**2) * (1.0 + 0.2 * np.cos(0.6 * x[i]))
        
        # Global conditioning with dynamic dimension scaling
        cond_factor = 1.0 + 0.4 * np.sin(0.3 * self.dim) + 0.2 * np.cos(0.5 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.25 * interference + 0.2 * rbf_cascade + 
                             0.25 * time_coupling + 0.15 * fractal_osc + 0.15 * exp_landscape)