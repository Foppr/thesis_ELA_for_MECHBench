import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Spherical quadratic basin
        spherical = np.sum(x_normalized**2)
        
        # Exponential decay components with varying rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.1 + 0.4 * np.sin(i * 0.5)
            exp_decay += np.exp(-rate * np.abs(x_normalized[i]))
        
        # Trigonometric oscillations with varying frequencies and phases
        trig_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.cos(i * 0.3)
            phase = 0.5 * np.sin(i * 0.7)
            trig_osc += np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Cross-dimensional coupling with gaussian interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x_normalized[i] - x_normalized[j])**2
                cross_coupling += np.exp(-dist / (2 * 0.2**2)) * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Multimodal sine-wave components with varying amplitudes
        multi_modal = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.cos(i * 0.4)
            freq = 3.0 + 2.0 * np.sin(i * 0.6)
            multi_modal += amp * np.sin(freq * x_normalized[i])**2
        
        # Add noise through a chaotic tent map
        noise = 0.0
        a = 1.5
        x_prev = 0.3
        for i in range(self.dim):
            if x_prev < 0.5:
                x_prev = a * x_prev
            else:
                x_prev = a * (1 - x_prev)
            noise += np.sin(x_prev * 8 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Combine all components with appropriate weights
        return 0.3 * spherical + 0.25 * exp_decay + 0.2 * trig_osc + 0.15 * cross_coupling + 0.08 * multi_modal + 0.02 * noise