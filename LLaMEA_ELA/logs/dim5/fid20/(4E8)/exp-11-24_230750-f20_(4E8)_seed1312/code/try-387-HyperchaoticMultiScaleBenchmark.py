import numpy as np

class HyperchaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic parameters with memory effects
        self.hurst = 0.1 + 0.8 * np.random.rand(dim)
        self.amplitude = 1.5 + 4.0 * np.random.rand(dim)
        self.frequency = 0.5 + 3.0 * np.random.rand(dim)
        self.memory_strength = 0.3 + 0.7 * np.random.rand(dim)
        # Multi-scale harmonic components
        self.harmonic_freqs = 2.0 + 5.0 * np.random.rand(4, dim)
        self.harmonic_amps = 0.5 + 2.0 * np.random.rand(4, dim)
        # Gaussian peak parameters with temporal dynamics
        self.gaussian_centers = np.random.uniform(-4, 4, (3, dim))
        self.gaussian_heights = 1.0 + 3.0 * np.random.rand(3)
        self.gaussian_widths = 0.5 + 2.0 * np.random.rand(3)
        # Temporal stiffness components
        self.stiffness_params = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic fractal component with memory
        fractal = 0.0
        for i in range(self.dim):
            noise = 0.0
            for k in range(1, 8):
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                # Add memory effect
                if k > 1:
                    amp *= (1.0 + self.memory_strength[i] * np.sin(0.1 * k))
                noise += amp * np.sin(freq * x[i])
            fractal += noise
            
        # Multi-scale harmonic potentials with temporal coupling
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(4):
                freq = self.harmonic_freqs[j, i]
                amp = self.harmonic_amps[j, i]
                # Temporal component
                temporal = 1.0 + 0.3 * np.sin(0.2 * x[i] + j)
                harmonic += amp * np.sin(freq * x[i]) * temporal
                
        # Dynamic Gaussian peaks with memory and temporal effects
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = self.gaussian_centers[j, i]
                height = self.gaussian_heights[j]
                width = self.gaussian_widths[j]
                # Memory effect
                memory_factor = 1.0 + 0.2 * np.sin(0.1 * x[i] + j)
                gaussian += height * np.exp(-0.5 * ((x[i] - center) / (width * memory_factor)) ** 2)
                
        # Cross-dimensional cubic couplings with adaptive stiffness
        cubic_coupling = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Adaptive stiffness
                stiffness = self.stiffness_params[i] + 0.1 * np.sin(0.3 * x[i])
                cubic_coupling += stiffness * (x[i] ** 3) * (x[i+1] ** 2)
                
        # Deceptive gradient landscape with exponential conditioning
        deceptive = 0.0
        for i in range(self.dim):
            # Exponential conditioning
            cond_factor = np.exp(0.1 * x[i])
            # Deceptive sine modulation
            deceptive += cond_factor * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i])
            
        # Multi-scale chaotic modulation with hyperchaos
        chaotic = 0.0
        for i in range(self.dim):
            chaos_freq = 10.0 + 20.0 * np.random.rand()
            chaos_amp = 0.5 + 1.5 * np.random.rand()
            chaotic += chaos_amp * np.sin(chaos_freq * x[i]) * np.cos(0.7 * x[i])
            
        # Combine all components with dimension-dependent scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim)
        return (0.25 * fractal + 0.20 * harmonic + 0.15 * gaussian + 
                0.20 * cubic_coupling + 0.15 * deceptive + 0.05 * chaotic) * dim_factor