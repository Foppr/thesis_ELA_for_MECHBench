import numpy as np

class FractalChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal mapping parameters for deterministic basins
        self.fractal_depths = np.random.uniform(0.5, 3.0, size=dim)
        self.fractal_scales = np.random.uniform(0.1, 1.0, size=dim)
        self.fractal_exponents = np.random.uniform(0.3, 0.8, size=dim)
        # Chaotic parameters for stochastic perturbations
        self.chaos_r = np.random.uniform(3.5, 4.0, size=dim)
        self.chaos_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Basin structure parameters with self-similarity
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=(5, dim))
        self.basin_radii = np.random.uniform(0.5, 2.0, size=5)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=5)
        # Dimensionality-dependent coupling strength
        self.coupling_strength = np.random.uniform(0.1, 1.5, size=dim)
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(1.0, 10.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.5, 3.0, size=dim)
        # Fractal dimension scaling factor
        self.fractal_dim_factor = np.random.uniform(0.5, 2.0, size=dim)
        # Dynamic perturbation parameters
        self.perturbation_magnitude = np.random.uniform(0.1, 0.5, size=dim)
        self.perturbation_frequency = np.random.uniform(0.5, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin component with self-similarity
        basin_component = 0.0
        for i in range(5):
            # Calculate distance to each basin center
            dist = np.sum((x - self.basin_centers[i]) ** 2)
            radius = self.basin_radii[i]
            depth = self.basin_depths[i]
            
            if dist <= radius:
                # Fractal-like basin shape with scaling
                normalized_dist = dist / radius
                fractal_shape = 1.0 - (normalized_dist ** self.fractal_exponents[i])
                basin_component += depth * fractal_shape
                
        # Chaotic perturbation component
        chaos_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence
            chaos_val = self.chaos_x0[i]
            for _ in range(20):
                chaos_val = self.chaos_r[i] * chaos_val * (1 - chaos_val)
            
            # Apply fractal scaling to chaos
            scaled_chaos = chaos_val ** self.fractal_exponents[i]
            chaos_component += scaled_chaos
            
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freqs[i] * (1 + 0.1 * np.sin(0.5 * x[i]))
            amp = self.harmonic_amps[i] * (1 + 0.2 * np.cos(0.3 * x[i]))
            harmonic_component += amp * np.sin(freq * x[i])
            
        # Dimensionality-dependent coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_val = self.coupling_strength[i] * self.coupling_strength[j]
                coupling_component += coupling_val * np.sin(x[i] - x[j])
                
        # Fractal dimension scaling effect
        fractal_dim_component = 0.0
        for i in range(self.dim):
            scale_factor = self.fractal_dim_factor[i] ** (self.dim / 10.0)
            fractal_dim_component += scale_factor * np.sin(x[i] ** 2)
            
        # Dynamic perturbation component
        perturbation_component = 0.0
        for i in range(self.dim):
            pert_val = self.perturbation_magnitude[i] * np.sin(
                self.perturbation_frequency[i] * x[i] + 
                np.cos(0.1 * x[i])
            )
            perturbation_component += pert_val
            
        # Combine all components with appropriate weights
        total = (
            1.5 * basin_component +
            1.2 * chaos_component +
            1.0 * harmonic_component +
            0.8 * coupling_component +
            0.6 * fractal_dim_component +
            0.4 * perturbation_component
        )
        
        return total