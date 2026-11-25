import numpy as np

class FractalGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fractal_amp = np.random.uniform(1.0, 5.0, size=dim)
        self.fractal_freq = np.random.uniform(0.5, 3.0, size=dim)
        # Adaptive gradient field parameters
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_decay = np.random.uniform(0.1, 1.5, size=dim)
        self.gradient_center = np.random.uniform(-4.0, 4.0, size=dim)
        # Saddle-point region parameters
        self.saddle_centers = np.random.uniform(-4.5, 4.5, size=(3, dim))
        self.saddle_strength = np.random.uniform(1.0, 4.0, size=3)
        self.saddle_radius = np.random.uniform(0.5, 2.0, size=3)
        # Multi-scale harmonic modulation
        self.harmonic_freq = np.random.uniform(1.0, 6.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.5, 2.5, size=dim)
        # Dimensional scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        # Noise parameters for terrain roughness
        self.noise_level = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_freq = np.random.uniform(0.5, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm_component = 0.0
        for i in range(self.dim):
            # Simple fractal sum using multiple frequencies
            fbm_val = 0.0
            for k in range(1, 6):
                freq = self.fractal_freq[i] * (2 ** k)
                amp = self.fractal_amp[i] / (2 ** (k * self.hurst[i]))
                fbm_val += amp * np.sin(freq * x[i])
            fbm_component += fbm_val
            
        # Adaptive gradient field component
        grad_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i] - self.gradient_center[i])
            grad_val = self.gradient_magnitude[i] * np.exp(-dist_from_center / self.gradient_decay[i])
            grad_component += grad_val
            
        # Saddle-point regions with repulsive forces
        saddle_component = 0.0
        for s in range(3):
            dist = np.sqrt(np.sum((x - self.saddle_centers[s]) ** 2))
            if dist <= self.saddle_radius[s]:
                # Repulsive force from saddle point
                force = self.saddle_strength[s] * (1 - dist / self.saddle_radius[s])
                saddle_component += force
                
        # Harmonic modulation component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amp[i] * np.cos(self.harmonic_freq[i] * x[i])
            harmonic_component += harmonic_val
            
        # Dimensional scaling and noise
        scale_component = 0.0
        noise_component = 0.0
        for i in range(self.dim):
            scale_component += self.scale_factors[i] * (x[i] ** 2)
            noise_component += self.noise_level[i] * np.sin(self.noise_freq[i] * x[i])
            
        # Combine all components with carefully tuned weights
        return (1.5 * fbm_component + 
                1.3 * grad_component + 
                1.2 * saddle_component + 
                1.1 * harmonic_component + 
                0.8 * scale_component + 
                0.6 * noise_component)