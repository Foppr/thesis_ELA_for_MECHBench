import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.base_conditioning = 18.0
        self.frequency_modulation = 4.0
        self.rbf_width = 0.6
        self.chaos_factor = 0.9
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying conditioning with chaotic modulation
        self.time += 0.01
        time_factor = 1 + 0.4 * np.sin(self.time) * np.cos(self.time * 0.6)
        conditioning = self.base_conditioning * time_factor
        
        # Base quadratic term with chaotic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = conditioning * (1 + 0.5 * np.sin(i * 0.25 + self.time))
            result += condition * x[i]**2
            
        # Radial basis functions with time-varying centers
        rbf_sum = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(self.time + i * 0.6)
            rbf_sum += np.exp(-self.rbf_width * (x[i] - center)**2)
            
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic_wave = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulation * (1 + 0.6 * np.sin(i * 0.35 + self.time))
            amp = 2.0 * (1 + 0.3 * np.cos(i * 0.45 + self.time * 0.8))
            chaotic_wave += amp * np.sin(freq * x[i] + self.time * 0.4)
            
        # Cross-dimensional coupling with dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1 + 0.4 * np.sin(0.5 * (x[i] + x[j]) + self.time)
                cross_term += weight * np.exp(-0.25 * (x[i]**2 + x[j]**2))
                
        # Polynomial chaos with exponential decay
        poly_chaos = 0.0
        for i in range(self.dim):
            chaos_component = np.sin(x[i] * self.chaos_factor + self.time) * np.cos(x[i] * 0.6)
            poly_chaos += (x[i]**5 + x[i]**7) * np.exp(-0.2 * np.abs(x[i])) * chaos_component
            
        # Adaptive phase interactions with time-varying coupling
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.25 * (x[i] - x[j]) + self.time * 0.9)
                coupling = 1 + 0.3 * np.cos(self.time + i * 0.35)
                phase_interaction += coupling * np.exp(-0.35 * (x[i] - x[j])**2) * phase
                
        # Global scaling with chaotic modulation
        global_scale = 1 + 0.25 * np.sin(np.sum(x) * 0.35 + self.time * 0.45)
        
        return global_scale * (result + 0.25 * rbf_sum + 0.4 * chaotic_wave + 0.25 * cross_term + 0.35 * poly_chaos + 0.2 * phase_interaction)