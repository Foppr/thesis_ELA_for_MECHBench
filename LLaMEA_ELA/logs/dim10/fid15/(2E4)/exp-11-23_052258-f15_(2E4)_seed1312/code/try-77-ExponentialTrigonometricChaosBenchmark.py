import numpy as np

class ExponentialTrigonometricChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Exponential decay with chaotic sine modulation
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(10.0 * x + np.random.rand() * np.pi))
        
        # Multi-dimensional trigonometric chaos with varying frequencies
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i)
            trig_chaos += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.tan(0.5 * x[i])
        
        # Cross-dimensional interaction with varying coupling strengths
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.2 * (i + j))
                cross_interaction += coupling * x[i] * x[j] * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Multimodal component with varying amplitude and frequency
        multimodal = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(0.5 * i)
            freq = 2.0 + 0.8 * np.cos(0.4 * i)
            multimodal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Adaptive scaling based on dimensionality and local curvature
        scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sum(np.sin(x)**2)
        
        # Add noise component for increased complexity
        noise = 0.05 * np.sum(np.random.randn(self.dim) * x)
        
        return scale * (radial_term + exp_decay + trig_chaos + cross_interaction + multimodal) + noise