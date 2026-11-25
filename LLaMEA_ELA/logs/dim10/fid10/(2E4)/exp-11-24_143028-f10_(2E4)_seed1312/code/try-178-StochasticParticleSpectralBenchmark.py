import numpy as np

class StochasticParticleSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Particle system parameters
        self.particle_count = max(10, dim * 2)
        self.time_step = 0.01
        self.damping = 0.95
        
        # Spectral interference parameters
        self.spectral_freqs = np.random.uniform(0.5, 3.0, dim)
        self.spectral_amps = np.random.uniform(0.5, 2.0, dim)
        
        # Evolutionary fitness landscape parameters
        self.generation = 0
        self.mutation_rate = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Stochastic particle system component
        particle_sum = 0.0
        for i in range(min(5, self.dim)):  # Limit to first 5 dimensions for particle system
            # Simulate simple harmonic motion with stochastic perturbations
            pos = x[i]
            velocity = np.sin(self.generation * 0.1 + pos) * 0.5
            acceleration = -pos * 0.8 + np.random.normal(0, 0.1)
            
            # Particle energy contribution
            particle_sum += 0.5 * (velocity**2 + pos**2) + 0.3 * np.abs(acceleration)
        
        # Spectral wave interference component
        spectral_sum = 0.0
        for i in range(self.dim):
            # Create interference patterns using multiple frequencies
            wave1 = self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i])
            wave2 = self.spectral_amps[i] * np.cos(self.spectral_freqs[i] * x[i] * 1.5)
            wave3 = 0.5 * self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i] * 2.0)
            
            # Interference pattern
            spectral_sum += wave1 * wave2 + wave2 * wave3 + wave1 * wave3
            
        # Evolutionary fitness landscape component
        fitness_sum = 0.0
        for i in range(self.dim):
            # Dynamic fitness landscape with moving optima
            optimum_shift = np.sin(self.generation * 0.05 + i) * 2.0
            distance_to_optimum = x[i] - (optimum_shift + np.sin(i) * 1.5)
            
            # Fitness function with multiple peaks and valleys
            fitness_sum += (distance_to_optimum**4 + 
                          0.5 * np.sin(3 * distance_to_optimum) * 
                          np.exp(-0.1 * distance_to_optimum**2))
        
        # Cross-dimensional interaction terms
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                # Coupled oscillatory behavior
                coupling_strength = 0.3 * (1 + np.cos(x[i] - x[j]))
                interaction_sum += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Time-varying chaotic modulation
        chaotic_modulation = 0.0
        for i in range(self.dim):
            # Logistic map based on position and generation
            logistic_input = 3.8 * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_modulation += np.sin(self.generation * 0.2 + logistic_input) * 0.5
        
        # Multi-scale Gaussian components with dynamic centers
        gaussian_sum = 0.0
        for i in range(self.dim):
            # Multiple Gaussian peaks with time-varying positions and widths
            center = 3.0 * np.sin(self.generation * 0.1 + x[i] * 0.5)
            width = 0.8 + 0.4 * np.cos(x[i])
            gaussian_sum += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Final combined function
        result = particle_sum + spectral_sum + fitness_sum + interaction_sum + chaotic_modulation + gaussian_sum
        
        # Add dynamic scaling based on generation
        result *= (1.0 + 0.1 * np.sin(self.generation * 0.02))
        
        return result