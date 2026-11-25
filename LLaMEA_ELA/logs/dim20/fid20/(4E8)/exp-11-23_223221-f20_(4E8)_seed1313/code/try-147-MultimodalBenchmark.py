import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with chaotic scaling factors
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.3 * np.abs(x[i]))
            poly_term += 0.5 * (x[i] ** 5) * scale * np.exp(-0.4 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.4 * (1.0 + np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]))
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j])
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                freq = 4.0 + 2.0 * np.sin(0.5 * x[i]) + 1.5 * np.cos(0.7 * x[j])
                # Enhanced chaotic phase shift
                phase = 0.8 * np.sin(0.4 * x[i] + 0.8 * x[j]) + 0.3 * np.sin(1.5 * x[i] * x[j]) + 0.1 * np.sin(2.3 * x[i] + 0.9 * x[j])
                rot_term += 0.3 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.4, 1.2, 2.8, 5.7, 7.9, 9.3]
            decay = 0.0
            for f in freqs:
                # Adjusted exponential decay frequencies with enhanced chaos
                mod_freq = f * (1.0 + 0.5 * np.sin(1.3 * x[i]) * np.cos(1.1 * x[i]) + 0.2 * np.sin(2.1 * x[i]))
                # Slight modification to decay behavior with additional sine modulation
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i]) * (1.0 + 0.2 * np.sin(0.6 * x[i]) + 0.1 * np.cos(1.4 * x[i]))
            decay_term += 0.3 * decay
        
        # Basin boundary with irregular fractal-like irregularities and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.2:
                basin_term += 0.15 * x[i]**5 + 0.06 * np.sin(20 * x[i]) + 0.04 * np.random.rand() * (1.0 + 0.3 * np.sin(3.0 * x[i]))
            else:
                basin_term += 0.2 * np.abs(x[i])**2.8 + 0.07 * np.cos(10 * x[i]) + 0.03 * np.random.rand() * (1.0 + 0.2 * np.cos(2.5 * x[i]))
        
        # Chaotic sine-wave component with adaptive amplitude and enhanced noise
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.7 + 0.4 * np.sin(0.9 * x[i]) + 0.1 * np.cos(1.2 * x[i])
            chaos_term += amp * np.sin(200 * x[i]) * np.exp(-1.0 * x[i]**2) + 0.05 * np.random.rand() * (1.0 + 0.2 * np.sin(5.0 * x[i]))
        
        # Add additional ridge structure for increased gradient complexity with enhanced chaos
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.15 * np.sin(3.5 * x[i]) * np.cos(2.8 * x[i]) + 0.07 * np.sin(8.0 * x[i]) + 0.03 * np.random.rand()
        
        # Add novel noise injection mechanism
        noise_injection = 0.0
        for i in range(self.dim):
            noise_injection += 0.02 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) + 0.01 * np.random.rand()
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term + ridge_term + noise_injection