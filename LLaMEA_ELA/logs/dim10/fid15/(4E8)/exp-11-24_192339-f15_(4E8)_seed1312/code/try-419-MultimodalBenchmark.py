import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Eigenvalue-driven frequency modulation
        eigen_freq = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * x[i] + i * 0.3)
            eigen_freq += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Time-delayed chaotic coupling with memory effects
        delay_coupling = 0
        for i in range(self.dim):
            delayed_val = x[(i - 1) % self.dim] if i > 0 else x[-1]
            coupling_strength = 1.0 + 0.5 * np.cos(0.6 * x[i] + 0.3 * delayed_val)
            delay_coupling += coupling_strength * np.exp(-0.2 * (x[i] - delayed_val)**2)
        
        # Adaptive basin tunneling with dynamic potential wells
        tunneling = 0
        for i in range(self.dim):
            well_depth = 1.0 + 0.7 * np.sin(0.5 * x[i] + self.dim * 0.2)
            tunnel_prob = 0.5 + 0.5 * np.tanh(0.8 * x[i])
            tunneling += well_depth * tunnel_prob * np.exp(-0.3 * x[i]**2)
        
        # Temporal harmonic interference with dynamic phase shifts
        temporal = 0
        for i in range(self.dim):
            phase_shift = 0.1 * np.sin(0.7 * x[i] + self.dim * 0.4)
            temporal += np.sin(3.0 * x[i] + phase_shift) * np.cos(2.5 * x[i]**2 + phase_shift)
        
        # Non-stationary conditioning with time-varying scaling
        time_factor = 1.0 + 0.3 * np.sin(0.2 * self.dim + 0.5 * np.sum(x))
        
        # Combine components with optimized weights
        return time_factor * (0.25 * eigen_freq + 0.30 * delay_coupling + 
                             0.20 * tunneling + 0.25 * temporal)