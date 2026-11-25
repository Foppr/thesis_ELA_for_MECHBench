import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyperbolic tangent based conditioning with fractal-like scaling
        tanh_component = np.sum(np.tanh(x_scaled**3)) * np.exp(-0.5 * np.sum(x_scaled**2))
        
        # Discrete phase transition points with varying thresholds
        phase_transitions = 0.0
        for i in range(self.dim):
            threshold = 0.3 * np.sin(i * 0.7) + 0.4
            if x_scaled[i] > threshold:
                phase_transitions += (x_scaled[i] - threshold)**2.5
            elif x_scaled[i] < -threshold:
                phase_transitions += (-x_scaled[i] - threshold)**2.5
            else:
                phase_transitions += 0.1 * x_scaled[i]**4
        
        # Coupling terms with hyperbolic sine and cosine interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                coupling += np.sinh(x_scaled[i] * x_scaled[j]) * np.cosh(2 * x_scaled[i] + x_scaled[j])
        
        # Multi-scale oscillatory component with exponentially decaying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4) * (1 + 0.2 * np.sin(i * 0.5))
            amp = 1.0 / (1.0 + 0.1 * i**1.5)
            multi_scale += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Fractal-like self-similarity with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += (np.sin(10 * x_scaled[i]) + np.cos(5 * x_scaled[i])) * np.exp(-0.3 * np.abs(x_scaled[i]))
        
        # Asymmetric ridge and valley structure with polynomial modulation
        structure = 0.0
        for i in range(self.dim):
            structure += (x_scaled[i]**2 + 0.5 * x_scaled[i]**4) * np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[i])
        
        # Global scaling and combination
        return 1.8 * tanh_component + 1.2 * phase_transitions + 0.9 * coupling + 0.7 * multi_scale + 0.5 * fractal + 0.3 * structure