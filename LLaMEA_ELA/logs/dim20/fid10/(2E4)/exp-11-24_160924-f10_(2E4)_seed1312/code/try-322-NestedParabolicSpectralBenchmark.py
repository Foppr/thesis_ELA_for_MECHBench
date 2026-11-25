import numpy as np

class NestedParabolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Initialize nested parabolic wells with varying depths
        self.well_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.well_depths = np.random.uniform(1.0, 5.0, (dim, 3))
        self.well_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        
        # Initialize spectral band parameters
        self.band_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.band_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.band_phases = np.random.uniform(0.0, 2*np.pi, dim)
        
        # Initialize noise modulation parameters
        self.noise_levels = np.random.uniform(0.1, 0.5, dim)
        self.modulation_rates = np.random.uniform(0.1, 0.8, dim)
        
        # Initialize adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Nested parabolic wells
        for i in range(self.dim):
            xi = x[i]
            center1, center2, center3 = self.well_centers[i]
            depth1, depth2, depth3 = self.well_depths[i]
            width1, width2, width3 = self.well_widths[i]
            
            # Three nested parabolic wells
            well1 = depth1 * np.exp(-0.5 * ((xi - center1) / width1)**2)
            well2 = depth2 * np.exp(-0.5 * ((xi - center2) / width2)**2)
            well3 = depth3 * np.exp(-0.5 * ((xi - center3) / width3)**2)
            
            result += (well1 + well2 + well3)
        
        # Spectral band interactions
        for i in range(self.dim):
            xi = x[i]
            freq = self.band_frequencies[i]
            amp = self.band_amplitudes[i]
            phase = self.band_phases[i]
            
            # Multi-frequency spectral components
            spectral_term = amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase)
            spectral_term += 0.5 * amp * np.sin(2 * freq * xi + phase) * np.cos(2 * freq * xi + phase)
            spectral_term += 0.3 * amp * np.sin(3 * freq * xi + phase) * np.cos(3 * freq * xi + phase)
            
            result += spectral_term
            
        # Adaptive noise modulation
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            modulation_rate = self.modulation_rates[i]
            
            # Time-varying noise component
            noise = noise_level * np.sin(modulation_rate * xi) * np.cos(modulation_rate * xi)
            result += noise
            
        # Adaptive scaling and cross-dimensional coupling
        for i in range(self.dim):
            xi = x[i]
            scale_factor = self.scaling_factors[i]
            
            # Apply adaptive scaling
            result += 0.5 * scale_factor * xi**2
            
        # Cross-dimensional coupling with spectral interaction
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Coupling based on spectral frequencies
                freq_i = self.band_frequencies[i]
                freq_j = self.band_frequencies[j]
                
                coupling = 0.2 * np.sin(freq_i * xi + freq_j * xj) * np.cos(freq_i * xi - freq_j * xj)
                result += coupling
                
        # Global harmonic modulation
        global_harmonic = 0.0
        for i in range(self.dim):
            xi = x[i]
            global_harmonic += np.sin(4 * xi) + 0.3 * np.sin(8 * xi) + 0.1 * np.sin(12 * xi)
        result += 0.3 * global_harmonic
        
        # Add multi-scale ridge structures
        for i in range(self.dim):
            xi = x[i]
            ridge_term = 0.4 * np.sin(5 * xi) * np.cos(5 * xi) + 0.2 * np.sin(10 * xi) * np.cos(10 * xi)
            result += ridge_term
            
        return result