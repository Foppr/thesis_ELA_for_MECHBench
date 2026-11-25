import numpy as np

class TrigonometricRadialBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for trigonometric components
        self.trig_amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        self.trig_frequencies = np.random.uniform(1.0, 8.0, size=dim)
        self.trig_phases = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Generate radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        
        # Adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_frequencies = np.random.uniform(0.5, 5.0, size=dim)
        
        # Global scaling and bias terms
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.bias = np.random.uniform(-1.0, 1.0)
        
    def f(self, x):
        # Ensure input is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric component
        trig_component = 0.0
        for i in range(self.dim):
            trig_component += self.trig_amplitudes[i] * np.sin(self.trig_frequencies[i] * x[i] + self.trig_phases[i])
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance_squared = np.sum((x - center) ** 2)
            rbf_component += np.exp(-distance_squared / (2 * width ** 2))
        
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x[i])
        
        # Combine all components with appropriate weights
        result = (self.global_scale * (trig_component + rbf_component) + 
                 self.bias + 0.5 * noise_component)
        
        return result